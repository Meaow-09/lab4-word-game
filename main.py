import random
from dataclasses import dataclass, field
from enum import Enum


class GameState(Enum):
    """Game state machine states."""
    INIT = "INIT"
    PLAYING = "PLAYING"
    WON = "WON"
    LOST = "LOST"
    REPLAY_PROMPT = "REPLAY_PROMPT"
    EXIT = "EXIT"


@dataclass
class Game:
    """Core game data structure (logic layer - no I/O)."""
    secret_word: str = ""
    guessed_letters: set[str] = field(default_factory=set)
    max_lives: int = 6
    lives: int = 6
    state: GameState = GameState.INIT
    message: str = ""


# ============================================================================
# LOGIC LAYER (No I/O, pure functions)
# ============================================================================

def get_word_list() -> list[str]:
    """Return available words for the game."""
    return [
        "PYTHON", "HANGMAN", "PROGRAMMING", "ALGORITHM", "DATABASE",
        "FUNCTION", "VARIABLE", "COMPUTER", "DEVELOPER", "KEYBOARD",
        "RECURSION", "DEBUGGING", "TESTING", "FRAMEWORK", "LIBRARY"
    ]


def select_random_word() -> str:
    """Select a random word from the word list."""
    return random.choice(get_word_list())


def get_masked_word(secret_word: str, guessed_letters: set[str]) -> str:
    """
    Return masked word display (e.g., '_ A _ _ _ A _').
    Uses list comprehension + indexing (no string replacement).
    """
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )


def update_game_state(secret_word: str,
                      guessed_letters: set[str],
                      guess: str,
                      lives: int) -> tuple[bool, str, set[str], int]:
    """
    Process a player guess and update game state (pure logic, no I/O).
    
    Args:
        secret_word: The word to guess (uppercase).
        guessed_letters: Set of already-guessed letters.
        guess: Player input.
        lives: Remaining wrong guesses.
    
    Returns:
        (is_valid, message, new_guessed_letters, new_lives):
        - is_valid: True if guess was processed, False if rejected
        - message: Feedback message for UI to display
        - new_guessed_letters: Updated set of guessed letters
        - new_lives: Updated lives count
    """
    guess = guess.strip().upper()
    
    # Validation
    if len(guess) != 1 or not guess.isalpha():
        return False, "Error: Please guess a single letter.", guessed_letters, lives
    
    if guess in guessed_letters:
        return False, f"You already guessed '{guess}'.", guessed_letters, lives
    
    # Process valid guess
    new_guessed = guessed_letters | {guess}
    
    if guess not in secret_word:
        new_lives = lives - 1
        msg = f"Wrong! '{guess}' is not in the word."
        return True, msg, new_guessed, new_lives
    else:
        msg = f"Correct! '{guess}' is in the word."
        return True, msg, new_guessed, lives


def check_win(secret_word: str, guessed_letters: set[str]) -> bool:
    """Check if player has guessed all unique letters in the word."""
    return set(secret_word).issubset(guessed_letters)


def check_loss(lives: int) -> bool:
    """Check if player has lost (no lives left)."""
    return lives <= 0


def initialize_game() -> Game:
    """Create a fresh game instance."""
    game = Game()
    game.secret_word = select_random_word()
    game.guessed_letters = set()
    game.lives = game.max_lives
    game.state = GameState.PLAYING
    game.message = ""
    return game


# ============================================================================
# UI LAYER (I/O only, calls logic functions)
# ============================================================================

def display_game_state(game: Game) -> None:
    """Display current game state to the player."""
    print("\n" + "="*60)
    print(f"Word: {get_masked_word(game.secret_word, game.guessed_letters)}")
    print(f"Lives: {game.lives}/{game.max_lives}")
    guessed_str = ", ".join(sorted(game.guessed_letters)) if game.guessed_letters else "None"
    print(f"Guessed letters: {guessed_str}")
    if game.message:
        print(f"➜ {game.message}")
    print("="*60)


def display_end_game(game: Game) -> None:
    """Display the game result."""
    print("\n" + "="*60)
    if game.state == GameState.WON:
        print(f"🎉 You won! The word was: {game.secret_word}")
    else:
        print(f"💀 You lost! The word was: {game.secret_word}")
    print("="*60)


def get_player_guess() -> str:
    """Get a letter guess from the player."""
    return input("\nGuess a letter: ")


def ask_replay() -> bool:
    """Ask the player if they want to play again."""
    response = input("\nPlay again? (yes/no): ").strip().lower()
    return response in ["yes", "y"]


# ============================================================================
# CONTROL LAYER (State machine - no while True)
# ============================================================================

def process_turn(game: Game) -> None:
    """
    Process one turn: get input, update state, check end conditions.
    Mutates game object.
    """
    guess = get_player_guess()
    is_valid, message, new_guessed, new_lives = update_game_state(
        game.secret_word,
        game.guessed_letters,
        guess,
        game.lives
    )
    
    game.message = message
    game.guessed_letters = new_guessed
    game.lives = new_lives
    
    # Check win/loss conditions
    if check_win(game.secret_word, game.guessed_letters):
        game.state = GameState.WON
    elif check_loss(game.lives):
        game.state = GameState.LOST


def run_game_state(game: Game) -> None:
    """
    State dispatcher (replaces while True).
    Processes game states sequentially using a state table.
    """
    state_handlers = {
        GameState.PLAYING: lambda g: (display_game_state(g), process_turn(g)),
        GameState.WON: lambda g: (display_end_game(g), setattr(g, 'state', GameState.REPLAY_PROMPT)),
        GameState.LOST: lambda g: (display_end_game(g), setattr(g, 'state', GameState.REPLAY_PROMPT)),
        GameState.REPLAY_PROMPT: lambda g: replay_handler(g),
        GameState.EXIT: lambda g: None,
    }
    
    # Process states until EXIT
    while game.state != GameState.EXIT:
        handler = state_handlers.get(game.state, lambda g: None)
        handler(game)


def replay_handler(game: Game) -> None:
    """Handle replay prompt and transition to next state."""
    if ask_replay():
        new_game = initialize_game()
        # Copy reference to same object to maintain loop
        game.secret_word = new_game.secret_word
        game.guessed_letters = new_game.guessed_letters
        game.lives = new_game.lives
        game.state = new_game.state
        game.message = new_game.message
    else:
        game.state = GameState.EXIT


# ============================================================================
# ENTRY POINT
# ============================================================================

def main() -> None:
    """Start the game."""
    print("Welcome to Hangman!")
    print("Guess the word one letter at a time.")
    game = initialize_game()
    run_game_state(game)
    print("Thanks for playing!")


if __name__ == "__main__":
    main()



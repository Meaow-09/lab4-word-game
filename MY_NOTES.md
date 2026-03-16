# My Original Thinking

## States

1. init
   pick a random word, telling the player the length of the word
2. guessing (circulate)
   ask for input, and telling player which letters are correct, wrong, and includes but at a wrong position, or win/failed
3. result
   how many time did the player used, how many times user guess, success or failed

## Variables

- dictionary of words
- chances for guessing
- selected word
- time used
- chances used
- display_word: str (or list) — visible pattern like _ a _ g _ a n.
- current status

## Rules and Invariants

Rules just like regular Hangman games

- A round starts with one fixed secret_word and attempts_left = max_attempts.
- Each turn accepts one guess (usually one alphabetic letter, normalized to lowercase).
- Invalid input (empty, non-letter, >1 char) does not change game progress.
- Repeated guess does not change game progress (or you define a penalty, but be consistent).
- Correct guess reveals all positions of that letter in the word.
- Wrong guess reduces attempts_left by exactly 1.
- Player wins when all unique letters in secret_word are guessed.
- Player loses when attempts_left == 0 and win condition is not met.
- After WON or LOST, no gameplay mutation should happen until reset/new game.

## Bugs and Edge cases

Numbers input, very long input, difficult word

- Duplicate guess penalty bug: repeated wrong guess decrements lives again when it should not.
- Unicode/locale bug: accented letters (é) fail isalpha() assumptions or normalization rules.

## CoPilot Suggestions

### App States

A minimal flow is:
INIT -> WAITING_FOR_GUESS -> VALIDATING_INPUT -> APPLYING_GUESS -> CHECKING_END_CONDITION -> (WAITING_FOR_GUESS | WON | LOST) -> GAME_OVER

### App Variables

For a basic Hangman, track these variables:

- secret_word: str — the word to guess.
- guessed_letters: set[str] — letters the player has tried.
- correct_letters: set[str] — guessed letters that are in secret_word (can be derived, but useful).
- wrong_letters: set[str] — guessed letters not in secret_word.
- max_attempts: int — allowed wrong guesses (e.g., 6).
- attempts_left: int — remaining wrong guesses.
- display_word: str (or list) — visible pattern like _ a _ g _ a n.
- game_state — one of your states (WAITING_FOR_GUESS, WON, LOST, etc.).

### App Rules and Invariants

Rules (Hangman)

- A round starts with one fixed secret_word and attempts_left = max_attempts.
- Each turn accepts one guess (usually one alphabetic letter, normalized to lowercase).
- Invalid input (empty, non-letter, >1 char) does not change game progress.
- Repeated guess does not change game progress (or you define a penalty, but be consistent).
- Correct guess reveals all positions of that letter in the word.
- Wrong guess reduces attempts_left by exactly 1.
- Player wins when all unique letters in secret_word are guessed.
- Player loses when attempts_left == 0 and win condition is not met.
- After WON or LOST, no gameplay mutation should happen until reset/new game.

### App Bugs

- Case mismatch: secret word is lowercase but guesses are uppercase (A vs a) and valid hits are missed.
- Whitespace/punctuation handling: words like "ice-cream" or "new york" break reveal/win logic if non-letters are treated like hidden letters.
- Duplicate guess penalty bug: repeated wrong guess decrements lives again when it should not.
- Duplicate tracking bug: guess goes into both correct_letters and wrong_letters due to bad branching.
- Input length bug: multi-character input ("ab") accepted as a single guess, corrupting state.
- Unicode/locale bug: accented letters (é) fail isalpha() assumptions or normalization rules.
- Off-by-one attempts: player loses one turn too early/late (<= 0 vs == 0 checks in the wrong place).
- Reveal bug: correct letter reveals only first occurrence instead of all positions.
- Win-condition bug: checking set(display_word) == set(secret_word) can fail because of _/spaces separators.
- Wrong invariant update order: state checked for win/loss before updating guessed sets, causing one-turn delay.
- Game-over mutation: guesses still modify state after WON/LOST.
- Reset/replay bug: new game reuses old guessed_letters or old attempts_left.
- Random-word selection bug: empty word list or invalid index crashes at startup.
- Display desync: rendered masked word not recomputed after each guess, so UI and internal state disagree.
- Scoring/statistics drift: wins/losses increment in both end-check and replay handler (double count).

## Observations

#### Did CoPilot overcomplicate or under-specify?

No, I think it response in a proper way, maybe due to the files in `.github`, they made AI changes a lot.

#### Does that help? In what way?

For sure, AI thinks more calm and comprehensive than me. Especially help me due to my bad English.

And I'm not familiar with Hangman games.

## Auto Play

### Initial analysis

A function to input random things in to the console, test the game.

### Design decisions

Add a mode switch for player to choose


# Guess The Word - Hangman Game

A Python implementation of the classic **Hangman word-guessing game** for the `AI 4 SE` class.

## Overview

In this game, the computer picks a random word, and you have a limited number of incorrect guesses to figure out what it is. Guess letters one at a time—if the letter is in the word, it's revealed. If not, you lose a life. Can you guess the word before running out of lives?

---

## Features

✨ **Core Gameplay**
- Random word selection from a curated word list
- Masked word display (e.g., `P Y _ _ O _`)
- Live counter (default: 6 incorrect guesses allowed)
- Track all guessed letters
- Instant win/loss detection

🎮 **User Experience**
- Clean, formatted console UI
- Clear feedback on each guess (correct/wrong/invalid)
- Replay support without restarting the program
- Graceful input validation

🏗️ **Architecture**
- **Separation of concerns**: Logic layer (pure functions) separate from UI layer
- **No while loops**: State machine dispatcher for game loop control
- **No string replacement**: Masked word built via list comprehension
- **Fully testable**: 13+ unit tests with 100% pass rate

---

## Installation

### Requirements
- Python 3.9+
- pytest (for running tests)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Meaow-09/lab4-word-game.git
   cd lab4-word-game
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies for test (optional)**
   
   ```bash
   pip install pytest
   ```

---

## How to Play

### Starting the Game

Run the game from the command line:

```bash
python3 main.py
```

### Gameplay Loop

1. **View the masked word** — See which letters you've guessed and which are still hidden
2. **Guess a letter** — Type a single alphabetic character (a–z, case-insensitive)
3. **Check feedback** — See if your guess was correct or wrong
4. **Track your lives** — Watch your remaining attempts decrease with each wrong guess
5. **Win or lose** — Either reveal all letters (win) or run out of lives (lose)
6. **Play again** — After each game, choose to play again or exit

### Example Game Session

```
Welcome to Hangman!
Guess the word one letter at a time.

============================================================
Word: P Y _ _ _ N
Lives: 6/6
Guessed letters: A, E, P, Y, N
➜ Correct! 'Y' is in the word.
============================================================

Guess a letter: o
```

---

## Game Rules

### Valid Moves
- ✅ Guess a **single alphabetic letter** (a–z or A–Z)
- ✅ Whitespace is automatically trimmed
- ✅ Case is normalized (uppercase internally)

### Invalid Moves (Rejected)
- ❌ Multi-character input (`"AB"` or `"123"`)
- ❌ Non-alphabetic characters (`"*"`, `"3"`, `"!"`)
- ❌ Empty input (`""`)
- ❌ Duplicate guesses (already tried letters)

### Scoring & End Conditions
| Condition | Result |
|-----------|--------|
| Guess all unique letters in the word | **WIN** 🎉 |
| Lives reach 0 before revealing all letters | **LOSE** 💀 |
| Any invalid input | No state change; game continues |

### Lives System
- **Start with**: 6 lives
- **Each wrong guess**: -1 life
- **Each correct guess**: Lives unchanged
- **Invalid/duplicate guesses**: Lives unchanged

---

## Project Structure

```
lab4-word-game/
├── main.py                 # Main game implementation
├── tests/
│   └── test_main.py        # Unit tests (13 tests, all passing)
├── README.md               # This file
├── .github/
│   ├── copilot-instructions.md
│   └── agents/
│       └── journal-logger.agent.md
├── JOURNAL.md              # Development journal
└── requirements.txt        # Python dependencies
```

### Code Organization (main.py)

The implementation follows a **three-layer architecture**:

#### 1. Logic Layer (Pure Functions)
No I/O or side effects. Core game mechanics:
- `update_game_state()` — Process a guess and return new state
- `check_win()` — Detect if player has won
- `check_loss()` — Detect if player has lost
- `get_masked_word()` — Build masked display (no `.replace()`)
- `initialize_game()` — Create fresh game instance

#### 2. UI Layer (Input/Output)
All user interaction:
- `display_game_state()` — Show current word, lives, guesses
- `display_end_game()` — Show win/loss result
- `get_player_guess()` — Capture player input
- `ask_replay()` — Ask if player wants to play again

#### 3. Control Layer (State Machine)
Orchestrates gameplay without loops:
- `run_game_state()` — State dispatcher using handler table
- `replay_handler()` — Handle replay logic
- `process_turn()` — Execute one game turn

#### Game State Enum
```python
INIT → PLAYING → (WON or LOST) → REPLAY_PROMPT → (PLAYING or EXIT)
```

---

## How to Run Tests

### Run All Tests
```bash
python3 -m pytest
```

### Run with Verbose Output
```bash
python3 -m pytest -v
```

### Run Specific Test
```bash
python3 -m pytest tests/test_main.py::test_correct_guess_keeps_lives -v
```

### Test Coverage
The test suite covers:
- ✅ Correct and wrong guess handling
- ✅ Invalid input rejection
- ✅ Duplicate guess detection
- ✅ Case-insensitive matching
- ✅ Win/loss condition detection
- ✅ Masked word generation
- ✅ State transitions

All **13 tests pass** with 100% success rate.

---

## Technical Design Decisions

### Why `set[str]` for guessed letters?
- O(1) membership check vs O(n) for lists
- Automatic duplicate prevention
- Clean set operations (`|` for union)

### Why no `.replace()` for masking?
- List comprehension + indexing is more explicit and educational
- Demonstrates functional thinking
- Avoids string manipulation pitfalls

### Why no `while True` loop?
- State machine is more maintainable and testable
- Clear state transitions make logic easier to follow
- Enables deterministic testing

### Why separate logic from UI?
- Logic can be tested independently without mocking I/O
- UI can be swapped (e.g., Flask web interface) without changing game logic
- Pure functions are easier to reason about

---

## Example Development Workflow

### Adding a New Word List Feature
1. Edit `get_word_list()` in the Logic Layer
2. Add test in `tests/test_main.py`
3. Run `python3 -m pytest`
4. No changes needed in UI or Control layers ✅

### Changing UI (e.g., colored output)
1. Modify `display_game_state()` in the UI Layer
2. No changes needed in Logic or Control layers ✅

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `Command 'pytest' not found` | Install: `pip install pytest` |
| Game won't start | Ensure Python 3.9+: `python3 --version` |
| Tests fail | Run from project root: `cd lab4-word-game && python3 -m pytest` |
| Invalid input causes crash | Check `update_game_state()` validation logic |

---

## Author

Built for **EPITA AI 4 SE** class  
Project Lab 4: Word Guess Game

---

## License

This project is for educational purposes as part of curriculum.


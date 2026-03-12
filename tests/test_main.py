# tests/test_main.py
from main import update_game_state, get_masked_word, check_win, check_loss


def test_wrong_guess_decrements_life_and_appends():
    """Correct guess should add letter and not decrement lives."""
    letters = {"A", "B"}
    is_valid, msg, new_letters, new_lives = update_game_state("HELLO", letters, "C", 5)
    assert is_valid is True
    assert new_lives == 4
    assert "C" in new_letters


def test_correct_guess_keeps_lives():
    """Correct guess should add letter and not decrement lives."""
    letters = {"A", "B"}
    is_valid, msg, new_letters, new_lives = update_game_state("HELLO", letters, "L", 5)
    assert is_valid is True
    assert new_lives == 5
    assert "L" in new_letters


def test_invalid_symbol_does_not_change_state():
    """Invalid input (* symbol) should not be processed."""
    letters = {"A", "B"}
    is_valid, msg, new_letters, new_lives = update_game_state("HELLO", letters, "*", 5)
    assert is_valid is False
    assert new_lives == 5
    assert new_letters == letters


def test_duplicate_guess_does_not_change_state():
    """Duplicate guess should not be processed."""
    letters = {"A", "B"}
    is_valid, msg, new_letters, new_lives = update_game_state("HELLO", letters, "A", 5)
    assert is_valid is False
    assert new_lives == 5
    assert new_letters == letters


def test_case_insensitive_match_against_secret_word():
    """Lowercase guess 'h' should match uppercase secret word 'Hello'."""
    letters = {"A", "B"}
    is_valid, msg, new_letters, new_lives = update_game_state("Hello", letters, "h", 5)
    assert is_valid is True
    assert new_lives == 5
    assert "H" in new_letters


def test_empty_string_input_is_invalid():
    """Empty string should be rejected."""
    letters = {"A", "B"}
    is_valid, msg, new_letters, new_lives = update_game_state("HELLO", letters, "", 5)
    assert is_valid is False
    assert new_lives == 5
    assert new_letters == letters


def test_multi_char_input_is_invalid():
    """Multi-character input should be rejected."""
    letters = {"A", "B"}
    is_valid, msg, new_letters, new_lives = update_game_state("HELLO", letters, "AB", 5)
    assert is_valid is False
    assert new_lives == 5
    assert new_letters == letters


def test_get_masked_word_reveals_guessed_letters():
    """Masked word should reveal only guessed letters."""
    secret = "PYTHON"
    guessed = {"P", "O"}
    masked = get_masked_word(secret, guessed)
    assert masked == "P _ _ _ O _"


def test_check_win_when_all_letters_guessed():
    """Should detect win when all unique letters are guessed."""
    secret = "CAT"
    guessed = {"C", "A", "T"}
    assert check_win(secret, guessed) is True


def test_check_win_when_not_all_letters_guessed():
    """Should not detect win when not all letters guessed."""
    secret = "CAT"
    guessed = {"C", "A"}
    assert check_win(secret, guessed) is False


def test_check_loss_when_lives_zero():
    """Should detect loss when lives reach 0."""
    assert check_loss(0) is True


def test_check_loss_when_lives_negative():
    """Should detect loss when lives go negative."""
    assert check_loss(-1) is True


def test_check_loss_when_lives_positive():
    """Should not detect loss when lives remain positive."""
    assert check_loss(1) is False

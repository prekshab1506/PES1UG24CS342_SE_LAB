import pytest
from tennis_scoring import game_score, set_winner, match_status


def test_game_score_normal():
    assert game_score(0, 0) == "0-0"
    assert game_score(1, 2) == "15-30"


def test_game_score_negative_a():
    with pytest.raises(ValueError):
        game_score(-1, 0)


def test_game_score_negative_b():
    with pytest.raises(ValueError):
        game_score(0, -1)


def test_game_score_deuce():
    assert game_score(3, 3) == "deuce"


def test_game_score_game_a():
    assert game_score(5, 3) == "game A"
    assert game_score(4, 2) == "game A"


def test_game_score_game_b():
    assert game_score(3, 5) == "game B"
    assert game_score(2, 4) == "game B"


def test_game_score_advantage():
    assert game_score(4, 3) == "advantage A"
    assert game_score(3, 4) == "advantage B"


def test_set_winner_a():
    assert set_winner(6, 4) == "A"
    assert set_winner(7, 6) == "A"


def test_set_winner_b():
    assert set_winner(4, 6) == "B"
    assert set_winner(6, 7) == "B"


def test_set_undecided():
    assert set_winner(3, 2) is None


def test_match_status_a_wins():
    assert match_status(2, 0, 3) == "A wins"


def test_match_status_b_wins():
    assert match_status(0, 2, 3) == "B wins"


def test_match_status_decider():
    assert match_status(1, 1, 3) == "decider"


def test_match_status_in_progress():
    assert match_status(1, 0, 3) == "in progress"
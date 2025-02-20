import pytest

from src.score import update_score


def test_update_score():
    """Testar att poängen uppdateras korrekt."""
    score = 0

    score = update_score(10,score)
    assert score == 10 , f"Expected 10, got {score}"

    score = update_score(-5, score)
    assert score == 5, f"Expected 5, got {score}"


def test_game_over():
    """Testar att spelet avslutas när poängen är 0 eller negativ."""
    score = 5

    with pytest.raises(SystemExit):
        update_score(-5, score)

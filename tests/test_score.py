import pytest

from src.score import Score


def test_update_score():
    """Testar att poängen uppdateras korrekt."""
    score = Score()

    score.update_score(10)
    assert score.get_score() == 10 , f"Expected 10, got {score.get_score()}"

    score.update_score(-5)
    assert score.get_score() == 5, f"Expected 5, got {score.get_score()}"


def test_game_over():
    """Testar att spelet avslutas när poängen är 0 eller negativ."""
    score = Score()
    score.update_score(5)

    with pytest.raises(SystemExit):
        score.update_score(-5)

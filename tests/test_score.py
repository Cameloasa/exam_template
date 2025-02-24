import pytest

from src.score import Score


def test_score_initial_value():
    """Testar om poängen börjar på 50"""
    score = Score() # Startvärde = 50

    assert score.get_score() == 50, f"Expected score 50, got {score.get_score()}"


def test_update_score():
    """Testar att poängen uppdateras korrekt."""
    score = Score()

    score.update_score(10)

    assert score.get_score() == 60 , f"Expected 10, got {score.get_score()}"

    score.update_score(-5)
    assert score.get_score() == 55, f"Expected 5, got {score.get_score()}"


def test_game_over():
    """Testar att spelet avslutas när poängen är 0 eller negativ."""
    score = Score()
    score.update_score(-49) # Blir 0 → Ska avsluta spelet

    with pytest.raises(SystemExit):
        score.update_score(-2) #om vi försöker gå under 0

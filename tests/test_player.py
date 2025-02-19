from src.grid import Grid
from src.player import Player


def test_can_move():
    grid = Grid()
    player = Player(x=2, y=2)

    grid.set(3, 2, grid.wall)

    assert not player.can_move(3, 2, grid), "Player should not be able to move to a wall position"

    assert player.can_move(2,3, grid), "Player should be able to move to an empty position"
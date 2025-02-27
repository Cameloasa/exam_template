from src.grid import Grid
from src.pickups import fertile_soil, Item


def test_fertile_soil():
    """Testar att fertile_soil() lägger till ett nytt föremål efter 25 drag."""
    grid = Grid()

    initial_pickups = sum(1 for x in range(grid.width) for y in range(grid.height) if isinstance(grid.get(x, y), Item))

    fertile_soil(grid, 25)

    new_pickups = sum(1 for x in range(grid.width) for y in range(grid.height) if isinstance(grid.get(x, y), Item))

    assert new_pickups == initial_pickups + 1, "Fertile soil add a new item!"
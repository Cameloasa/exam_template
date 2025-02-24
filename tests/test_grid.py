from src.grid import Grid


def test_make_walls():
    """Testar funktionen make_walls"""
    grid = Grid()
    grid.make_walls()

    for x in range(grid.width):
        assert grid.get(x, 0) == grid.wall, f"Wall missing at (x={x}, y=0)"
        assert grid.get(x, grid.height - 1) == grid.wall, f"Wall missing at (x={x}, y={grid.height - 1})"

    for y in range(grid.height):
        assert grid.get(0, y) == grid.wall, f"Wall missing at (x=0, y={y})"
        assert grid.get(grid.width - 1, y) == grid.wall, f"Wall missing at (x={grid.width - 1}, y={y})"

    for x in range(1, grid.width - 1):
        for y in range(1, grid.height - 1):
            assert grid.get(x, y) == grid.empty, f"Unexpected wall at (x={x}, y={y})"
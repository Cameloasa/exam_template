from src.grid import Grid
from src.player import Player


def test_make_walls():
    """Testar funktionen make_walls"""
    grid = Grid()
    grid.make_walls()

    # Kontrollera väggarna
    for x in range(grid.width):
        assert grid.get(x, 0) == grid.wall, f"Wall missing at (x={x}, y=0)"
        assert grid.get(x, grid.height - 1) == grid.wall, f"Wall missing at (x={x}, y={grid.height - 1})"

    for y in range(grid.height):
        assert grid.get(0, y) == grid.wall, f"Wall missing at (x=0, y={y})"
        assert grid.get(grid.width - 1, y) == grid.wall, f"Wall missing at (x={grid.width - 1}, y={y})"

    # Kontrollera om det finns minst en inre vägg
    has_inner_wall = any(
        grid.get(x, y) == grid.wall
        for x in range(1, grid.width - 1)
        for y in range(1, grid.height - 1)
    )

    assert has_inner_wall, "No inner walls were created!"


def test_internal_walls():
    """Testar att make_walls() skapar inre väggar."""
    grid = Grid()
    grid.make_walls()

    internal_wall_found = False

    for y in range(1, grid.height - 1):
        for x in range(1, grid.width - 1):
            if grid.get(x, y) == grid.wall:
                internal_wall_found = True
                break
        if internal_wall_found:
            break

    assert internal_wall_found, "No internal walls were created."


def test_player_not_blocked():
    """Testar att spelaren inte är instängd av väggar."""
    grid = Grid()
    player = Player(5, 5)
    grid.set_player(player)
    grid.make_walls()

    player_x, player_y = grid.player.pos_x, grid.player.pos_y

    # Kontrollera om det finns minst en ledig väg runt spelaren
    free_path = any(
        grid.is_empty(player_x + dx, player_y + dy)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]
        if 0 < player_x + dx < grid.width - 1 and 0 < player_y + dy < grid.height - 1
    )

    assert free_path, "The player is completely blocked by walls!"
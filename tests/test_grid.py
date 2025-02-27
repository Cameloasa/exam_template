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

    # Kontrollera om det finns minst en inre vägg
    assert any(grid.get(x, y) == grid.wall for x in range(1, grid.width - 1)
                                          for y in range(1, grid.height - 1)), "No internal walls were created."


def test_player_not_blocked():
    """Testar att spelaren inte är instängd av väggar."""
    grid = Grid()
    grid.make_walls()  # Först skapar vi väggarna

    player = Player(5, 5)
    grid.set_player(player)  # Sedan sätter vi spelaren på kartan

    px, py = player.pos_x, player.pos_y

    # Kontrollera om det finns minst en ledig väg runt spelaren
    assert any(grid.is_empty(px + dx, py + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]), \
        "The player is completely blocked by walls!"

def test_place_traps():
    """Testar att fällor placeras korrekt på kartan."""
    grid = Grid()
    grid.place_traps(num_traps=3)

    trap_count = sum(row.count("X") for row in grid.data)  # Räknar antal "X"
    assert trap_count == 3, f"Expected 3 traps, but found {trap_count}"
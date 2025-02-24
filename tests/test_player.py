from src.grid import Grid
from src.player import Player


def test_can_move_horisontal():
    """Testar om spelaren flyttar en position till höger"""
    grid = Grid()
    player = Player(x=2, y=2)

    # Sätter en vägg till höger,
    grid.set(3, 2, grid.wall)

    # Testar horisontell rörelse
    assert not player.can_move(3, 2, grid), "Player should not be able to move to a wall position (right)"
    assert player.can_move(1, 2, grid), "Player should be able to move to an empty position (left)"


def test_can_move_vertical():
    """Testar om spelaren flyttar en position uppåt eller neråt"""
    grid = Grid()
    player = Player(x=2, y=2)

    # Sätter en vägg Ovanför och under
    grid.set(2, 1, grid.wall)  # Ovanför
    grid.set(2, 3, grid.wall)  # Under

    # Testar vertikal rörelse
    assert not player.can_move(2, 1, grid), "Player should not be able to move to a wall position (up)"
    assert not player.can_move(2, 3, grid), "Player should not be able to move to a wall position (down)"

def test_cannot_move_through_walls():
    """Testar att spelaren INTE kan gå genom väggar."""
    grid = Grid()
    player = Player(x=2, y=2)

    # Sätter väggar i alla riktningar
    grid.set(3, 2, grid.wall)  # Höger
    grid.set(1, 2, grid.wall)  # Vänster
    grid.set(2, 1, grid.wall)  # Uppåt
    grid.set(2, 3, grid.wall)  # Nedåt

    # Testar att spelaren INTE kan röra sig i någon riktning
    assert not player.can_move(3, 2, grid), "Player should NOT be able to move right into a wall"
    assert not player.can_move(1, 2, grid), "Player should NOT be able to move left into a wall"
    assert not player.can_move(2, 1, grid), "Player should NOT be able to move up into a wall"
    assert not player.can_move(2, 3, grid), "Player should NOT be able to move down into a wall"

def test_player_starts_in_the_middle():
    """Testar om player börjar i mitten av grid"""
    grid = Grid()
    middle_x = grid.width // 2
    middle_y = grid.height // 2

    player = Player(middle_x,middle_y)

    assert (middle_x - 1 <= player.pos_x <= middle_x + 1) and \
           (middle_y - 1 <= player.pos_y <= middle_y + 1), "Player should start near the middle"

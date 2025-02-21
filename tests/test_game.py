from src.game import move_player
from src.grid import Grid
from src.pickups import Item
from src.player import Player



def test_move_player():
    """Testar att spelaren rör sig korrekt och att poängen uppdateras."""
    """Initializer grid, player & score """
    player = Player(2,2)
    grid = Grid()
    grid.set_player(player)
    score = 0

    """Initializer item in grid """
    item = Item("apple", 10, "?")
    grid.set(3, 2, item)

    """Flyttar spelaren en position"""
    score = move_player(player, 1, 0, grid, score)

    assert player.pos_x == 2 and player.pos_y == 2, "Player should be at (2,2)"
    assert grid.get(3, 2) is None, "Item should be removed after pickup"

    score = move_player(player, -1, 0, grid, score)
    assert player.pos_x == 2 and player.pos_y == 2, "Player should be at (2,2)"
    assert grid.get(3, 2) is None, "Item should be removed after pickup"
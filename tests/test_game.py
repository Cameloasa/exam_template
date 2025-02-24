from src.game import move_player
from src.grid import Grid
from src.pickups import Item
from src.player import Player
from src.score import Score


def test_move_player_moves_correctly():
    """Testar att spelaren rör sig korrekt och att poängen uppdateras."""

    ##initializera grid, player och score, set player
    player = Player(2,2)
    grid = Grid()
    grid.set_player(player)
    score = Score()

    # move player till höger ett steg
    move_player(player, 1, 0, grid, score)  # Flyttar höger
    assert player.pos_x == 3 and player.pos_y == 2, "Player should be at (3,2)"

    # move player till västern ett steg
    move_player(player, -1, 0, grid, score)  # Flyttar vänster
    assert player.pos_x == 2 and player.pos_y == 2, "Player should be back at (2,2)"


def test_pickups_item_update_score():
    """Testar att poängen uppdateras när spelaren plockar upp ett föremål"""

    #initializera grid, player och score, set player
    player = Player(2, 2)
    grid = Grid()
    grid.set_player(player)
    score = Score()

    #set föremålet i grid
    item = Item("apple",10,"?")
    grid.set(3,2, item)

    #flyttar player till föremålet
    move_player(player,1,0,grid,score)

    assert score.get_score() == 10, f"Expected score 10, got score {score.get_score()}"

def test_item_is_removed_after_pickups():
    """Testar om föremålet tas up från grid efter player picks up """

    #initializera grid, player och score, set player
    player = Player(2, 2)
    grid = Grid()
    grid.set_player(player)
    score = Score()

    #set föremålet i grid
    item = Item("apple",10,"?")
    grid.set(3,2, item)

    # flyttar player till föremålet
    move_player(player, 1, 0, grid, score)

    assert grid.get(3, 2) is ".", "Item should be removed after pickup"












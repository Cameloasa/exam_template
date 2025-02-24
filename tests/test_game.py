from src.game import move_player
from src.grid import Grid
from src.pickups import Item
from src.player import Player
from src.score import Score


def test_pickups_item_add_to_inventory_and_remove_from_grid():
    """Testar att föremålet plockas upp, läggs till inventory och tas bort från grid"""

    #initializera grid, player, set player och inventory
    player = Player(2, 2)
    grid = Grid()
    grid.set_player(player)
    inventory = []


    #Placera föremålet på kartan
    item = Item("apple",20,"A")
    grid.set(3,2, item)

    #flyttar player till föremålet
    move_player(player,1,0,grid,Score(), inventory)

    # Kontrollera att föremålet är borta från kartan
    assert grid.get(3, 2) is None or grid.get(3, 2) == ".", "Item should be removed from the grid"

    # Kontrollera att föremålet är i inventory
    assert any(i.name == "apple" for i in inventory), "Item should be in inventory"


def test_score_decrease_each_step():
    #grid, player, set player och score
    player = Player(2, 2)
    grid = Grid()
    grid.set_player(player)
    score = Score()
    initial_score = score.get_score()

    # flyttar player ett steg till höger
    move_player(player, 1, 0, grid, score, [])
    assert score.get_score() == initial_score - 1, "Score should decrease by 1 per step"

    move_player(player, 0, 1, grid, score, [])  # Flyttar ner
    assert score.get_score() == initial_score - 2, "Score should decrease by 1 per step again"



















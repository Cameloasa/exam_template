from .grid import Grid
from .player import Player
from . import pickups
from src.score import print_status, update_score



player = Player(2, 1)
inventory = []
score = 0
grid = Grid()
grid.set_player(player)
grid.make_walls()
pickups.randomize(grid)


command = "a"
# Loopa tills användaren trycker Q eller X.
while not command.casefold() in ["q", "x"]:
    print_status(grid, score)

    command = input("Use WASD to move, Q/X to quit. ")
    command = command.casefold()[:1]

    if command == "d" and player.can_move(1, 0, grid):  # move right
        # TODO: skapa funktioner, så vi inte behöver upprepa så mycket kod för riktningarna "W,A,S"
        maybe_item = grid.get(player.pos_x + 1, player.pos_y)
        player.move(1, 0)

        if isinstance(maybe_item, pickups.Item):
            # we found something
            score += maybe_item.value
            print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
            #g.set(player.pos_x, player.pos_y, g.empty)
            grid.clear(player.pos_x, player.pos_y)


# Hit kommer vi när while-loopen slutar
print("Thank you for playing!")

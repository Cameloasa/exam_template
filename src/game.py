from src.grid import Grid
from src.player import Player
from src.pickups import pickups, randomize, Item
from src.score import print_status, update_score

def move_player(player, dx, dy, grid, score):
    """Försöker flytta spelaren och uppdatera poäng om det behövs."""

    new_x = player.pos_x + dx
    new_y = player.pos_y + dy

    if player.can_move(new_x, new_y, grid):  # kontrollera nästa position
        maybe_item = grid.get(new_x, new_y)
        player.move(dx, dy)

        if isinstance(maybe_item, Item):
            score = update_score(maybe_item.value, score)
            print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
            grid.clear(new_x, new_y)

    return score

player = Player(2, 1)
inventory = []
score = 0
grid = Grid()
grid.set_player(player)
grid.make_walls()
randomize(grid)

command = "a"
# Loopa tills användaren trycker Q eller X.
while not command.casefold() in ["q", "x"]:
    print_status(grid, score)

    command = input("Use WASD to move, Q/X to quit. ")
    command = command.casefold()[:1]

    moves = {"w": (0, -1),
             "a": (-1, 0),
             "s": (0, 1),
             "d": (1, 0)}
    if command in moves:
        dx, dy = moves[command]
        score = move_player(player, dx, dy, grid, score)

# Hit kommer vi när while-loopen slutar
print(f"Thank you for playing!Your final score is: {score}")

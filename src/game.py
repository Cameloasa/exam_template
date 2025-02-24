from src.grid import Grid
from src.player import Player
from src.pickups import pickups, randomize, Item
from src.score import Score


def move_player(player, dx, dy, grid, score):
    """Försöker flytta spelaren och uppdatera poäng om det behövs."""

    new_x = player.pos_x + dx
    new_y = player.pos_y + dy

    if player.can_move(new_x, new_y, grid):  # kontrollera nästa position
        maybe_item = grid.get(new_x, new_y)
        player.move(dx, dy)

        if isinstance(maybe_item, Item):
            score.update_score(maybe_item.value)
            print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
            grid.clear(new_x, new_y)


def main():
    """Huvudfunktion för spelet."""
    player = Player(2, 1)
    inventory = []
    score = Score()
    grid = Grid()
    grid.set_player(player)
    grid.make_walls()
    randomize(grid)

    command = "a"
    # Loopa tills användaren trycker Q eller X.
    while not command.casefold() in ["q", "x"]:
        print("--------------------------------------")
        print(f"You have {score.get_score()} points.")
        print(grid)

        command = input("Use WASD to move, Q/X to quit. ")
        command = command.casefold()[:1]

        moves = {"w": (0, -1),
                 "a": (-1, 0),
                 "s": (0, 1),
                 "d": (1, 0)}
        if command in moves:
            dx, dy = moves[command]
            move_player(player, dx, dy, grid, score)

    print(f"Thank you for playing! Your final score is: {score.get_score()}")


# Kör spelet endast om filen körs direkt
if __name__ == "__main__":
    main()

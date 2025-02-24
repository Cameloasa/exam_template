from src.grid import Grid
from src.player import Player
from src.pickups import pickups, randomize, Item
from src.score import Score


def move_player(player, dx, dy, grid, score, inventory):
    """Försöker flytta spelaren och uppdatera poäng om det behövs."""

    new_x = player.pos_x + dx
    new_y = player.pos_y + dy

    if player.can_move(new_x, new_y, grid):  # kontrollera nästa position
        maybe_item = grid.get(new_x, new_y)
        player.move(dx, dy)

        if isinstance(maybe_item, Item):
            inventory.append(maybe_item)  # Lägg till i inventory
            score.update_score(maybe_item.value)
            print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
            grid.clear(new_x, new_y)


def main():
    """Huvudfunktion för spelet."""
    # skapa grid
    grid = Grid()
    # skapa vägar
    grid.make_walls()
    # randomise pickups
    randomize(grid)

    # hämta mittenpositionen av grid
    middle_x = grid.width // 2
    middle_y = grid.height // 2

    # om det finns en vägg, flytta spelaren neråt
    if grid.get(middle_x, middle_y) == grid.wall:
        middle_y += 1

    #skapa player
    player = Player(middle_x,middle_y)
    # set player
    grid.set_player(player)
    # initiate score = 50
    score = Score()
    # initiate an empty list of pickups
    inventory = []




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
            move_player(player, dx, dy, grid, score,inventory)

        elif command == "i":
            print("\n--- Inventory ---")
            if inventory:
                for item in inventory:
                    print(f"- {item.name} ({item.symbol})")
            else:
                print("Your inventory is empty.")
            print("-----------------")

    print(f"Thank you for playing! Your final score is: {score.get_score()}")


# Kör spelet endast om filen körs direkt
if __name__ == "__main__":
    main()

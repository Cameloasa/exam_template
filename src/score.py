

def print_status(grid, score):
    """Visa spelvärlden och antal poäng."""
    print("--------------------------------------")
    print(f"You have {score} points.")
    print(grid)

def update_score(value, score): #maybe_item_value
    """Uppdatera poängen och returnera nytt värde."""
    score += value
    print(f"Your score is now: {score}")

    if score <= 0:
        print("Game Over! You lost all your points.")
        exit()

    return score
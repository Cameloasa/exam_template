

class Score:

    def __init__(self):
        self.value = 0

    def get_score(self):
        return self.value

    def update_score(self, amount):
        """Uppdatera poängen och returnera nytt värde."""
        self.value += amount

        if self.value <= 0:
            print("Game Over! You lost all your points.")
            exit()

    def __str__(self):
        """Visa spelvärlden och antal poäng."""
        return self.value




class Score:

    def __init__(self, start_value = 50 ):
        self.value = start_value

    def get_score(self):
        return self.value

    def update_score(self, points):
        """Uppdatera poängen och returnera nytt värde."""
        self.value += points

        if self.value <= 0:
            print("Game Over! You lost all your points.")
            exit()

    def __str__(self):
        """Visa spelvärlden och antal poäng."""
        return str(self.value)


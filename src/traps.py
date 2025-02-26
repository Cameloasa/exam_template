
class Trap:
    """Representerar en fälla som minskar spelarens poäng."""
    def __init__(self, value=-10, symbol = "X"):
        self.value = value
        self.symbol = symbol

    def __str__(self):
        return self.symbol

    def apply_effect(self, score):
        """Applicerar fällans effekt på spelaren (drar av poäng)."""
        score.update_score(self.value)



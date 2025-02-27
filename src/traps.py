
class Trap:
    """Representerar en fälla som minskar spelarens poäng."""
    def __init__(self, value=-10, symbol = "X"):
        self.value = value
        self.symbol = symbol

    def __str__(self):
        return self.symbol

    def apply_effect_traps(self, score):
        """Applicerar fällans effekt på spelaren (drar av 10 poäng)."""
        score.update_score(self.value)



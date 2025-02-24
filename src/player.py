class Player:
    marker = "@"

    def __init__(self, x, y):
        """Initialisera spelaren med en start position"""
        self.pos_x = x #horisontal
        self.pos_y = y #verical

    # Flyttar spelaren. "dx" och "dy" är skillnaden
    def move(self, dx, dy):
        """Flyttar spelaren.\n
        dx = horisontell förflyttning, från vänster till höger\n
        dy = vertikal förflyttning, uppifrån och ned"""
        self.pos_x += dx
        self.pos_y += dy


    def can_move(self, x, y, grid):
        """Kontrollerar om spelaren kan röra sig till positionen (x, y)."""
        if grid.get(x, y) == grid.wall:
            return False
        return True




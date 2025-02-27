import random

from src.traps import Trap


class Grid:
    """Representerar spelplanen. Du kan ändra standardstorleken och tecknen för olika rutor. """
    width = 36
    height = 12
    empty = "."  # Tecken för en tom ruta
    wall = "■"   # Tecken för en ogenomtränglig vägg

    def __init__(self):
        """Skapa ett objekt av klassen Grid"""
        # Spelplanen lagras i en lista av listor. Vi använder "list comprehension" för att sätta tecknet för "empty" på varje plats på spelplanen.
        self.data = [[self.empty for y in range(self.width)] for z in range(
            self.height)]


    def get(self, x, y):
        """Hämta det som finns på en viss position use in player can_move"""
        return self.data[y][x]

    def set(self, x, y, value):
        """Ändra vad som finns på en viss position"""
        self.data[y][x] = value

    def set_player(self, player):
        self.player = player #player Instance attribute player defined outside __init__  we use that in game.py

    def clear(self, x, y):
        """Ta bort item från position"""
        self.set(x, y, self.empty)

    def __str__(self):
        """Gör så att vi kan skriva ut spelplanen med print(grid)"""
        xs = ""
        for y in range(len(self.data)):
            row = self.data[y]
            for x in range(len(row)):
                if x == self.player.pos_x and y == self.player.pos_y:
                    xs += "@"
                else:
                    xs += str(row[x])
            xs += "\n"
        return xs


    def make_walls(self):
        """Skapa väggar runt hela spelplanen och inre väggar"""

        # Skapar yttre väggar
        for i in range(self.height):
            self.set(0, i, self.wall)
            self.set(self.width - 1, i, self.wall)

        for j in range(1, self.width - 1):
            self.set(j, 0, self.wall)
            self.set(j, self.height - 1, self.wall)

        # Skapar fasta inre väggar (exempel på symmetriska väggar)
        for x in range(3, self.width - 3, 4):  # Väggrader var fjärde kolumn
            for y in range(3, self.height - 3, 4):  # Var fjärde rad
                self.set(x, y, self.wall)
                self.set(x + 1, y, self.wall)  # Gör väggen bredare
                self.set(x, y + 1, self.wall)

    # Används i filen pickups.py
    def get_random_x(self):
        """Slumpa en x-position på spelplanen"""
        return random.randint(0, self.width-1)

    def get_random_y(self):
        """Slumpa en y-position på spelplanen"""
        return random.randint(0, self.height-1)

    def is_empty(self, x, y):
        """Returnerar True om det inte finns något på aktuell ruta"""
        return self.get(x, y) == self.empty

    def place_traps(self, num_traps=3):
        """Slumpar och placerar ut fällor på kartan."""
        for _ in range(num_traps):
            x, y = random.randint(1, self.width - 2), random.randint(1, self.height - 2)
            if self.is_empty(x, y):  # Undvik att lägga på väggar eller pickups
                self.set(x, y, Trap().symbol)  # Använder symbolen "X"


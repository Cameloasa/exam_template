

class Item:
    """Representerar saker man kan plocka upp."""
    def __init__(self, name, value=10, symbol="?"):
        self.name = name
        self.value = value
        self.symbol = symbol

    def __str__(self):
        return self.symbol


pickups = [Item("carrot", 20, "?"),
           Item("apple", 20, "?"),
           Item("strawberry", 20, "?"),
           Item("cherry", 20, "?"),
           Item("watermelon", 20, "?"),
           Item("radish", 20, "?"),
           Item("cucumber", 20, "?"),
           Item("meatball", 20, "?")]



def randomize(grid):
    for item in pickups:
        while True:
            # slumpa en position tills vi hittar en som är ledig
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, item)
                break  # avbryt while-loopen, fortsätt med nästa varv i for-loopen


def fertile_soil(grid, moves_count):
    """Efter varje 25:e drag skapas en ny frukt/grönsak på kartan."""
    if moves_count % 25 == 0:
        new_item = pickups[moves_count // 25 % len(pickups)]  # väljer en random pickup från Item
        while True:
            x, y = grid.get_random_x(), grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, new_item)
                print(f"A new {new_item.name} has grown on the map!")
                break  # avbryt while-loopen, fortsätt med nästa varv i for-loopen
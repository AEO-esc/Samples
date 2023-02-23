class Backpack:
    def __init__(self) -> None:
        self._backpack_items = []

    @property
    def backpack_items(self):
        return self._backpack_items
    @backpack_items.setter
    def backpack_items(self, new_items):
        if isinstance(new_items, list):
            self._backpack_items = new_items
        else:
            print("not a valid list.")

my_backpack = Backpack()
print(my_backpack.backpack_items)
my_backpack.backpack_items = ["Tape", "Pencil", "HP Laserjet"]
print(my_backpack.backpack_items)

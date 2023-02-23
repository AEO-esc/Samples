class Backpack:
    def __init__(self) -> None:
        self._backpack_items = []

    @property
    def backpack_items(self):
        return self._backpack_items
    
    def add_item(self, item):
        if isinstance(item, str):
            self._backpack_items.append(item)
        else:
            print(str, " is not a valid item.")
    def remove_item(self, item):
        if item in self._backpack_items:
            self._backpack_items.remove(item)
            return 1
        else:
            return 0
    
    def has_item(self, item):
        return item in self._backpack_items
    
def campingTrip() -> None:
    my_backpack = Backpack()
    print(my_backpack.backpack_items)

    my_backpack.add_item("Water Bottle")
    print(my_backpack.backpack_items)

    my_backpack.add_item("Sleeping Bag")
    print(my_backpack.backpack_items)

    my_backpack.add_item("Thermo")
    print(my_backpack.backpack_items)

    my_backpack.remove_item("Sleeping Bag")
    print(my_backpack.backpack_items)



def main() -> None:
    # going on a camping trip
    campingTrip()

if __name__ == "__main__":
    main()
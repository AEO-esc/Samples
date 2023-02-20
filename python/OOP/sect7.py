class Movie:
    def __init__(self, title, rating) -> None:
        self._title = title
        self._rating = rating

    def get_title(self):
        return self._title
    # with setters, we can vaildate the values before setting them 
    # helps us protect class attributes from bad data
    def set_title(self, new_title):
        # only accept string names and only letters
        if isinstance(new_title, str) and new_title.isalpha():
            self._title = new_title
        else:
            print("Bad title: ", new_title, " Try again.")

class Backpack:
    def __init__(self) -> None:
        self._items = []

    def get_items(self):
        return self._items
    def set_items(self, new_items):
        # check to see if we received a list then add it
        if isinstance(new_items, list):
            self._items = new_items
        else:
            print("Please enter a valid list of items.")

class Circle:
    def __init__(self, radius) -> None:
        self._radius = radius
    def get_radius(self):
        return self._radius;
    def set_radius(self, new_radius):
        if isinstance(self, float) and new_radius > 0:
            self._radius = new_radius
        else:
            print("Not a valid radius.")
    def get_circumerference(self):
        return self._radius * 3.14159

    
def main() -> None:
    my_Movie = Movie("The Godfather", 4.8)
    # using the getter for title 
    print(my_Movie.get_title())
    my_Movie.set_title("^&*ASD")
    print(my_Movie.get_title())

    my_backpack = Backpack()
    my_backpack.set_items(["Water Bottle", "Notebook", "Pens", "Pencils"])
    print(my_backpack.get_items())

    my_circle = Circle(5.6)
    print(my_circle.get_radius())
    my_circle.set_radius(-1)
    print(my_circle.get_radius(), " ", my_circle.get_circumerference())

if __name__ == "__main__":
    main();
class Circle:

    VALID_COLORS = ("Red", "Blue", "Green")

    def __init__(self, radius, color) -> None:
        self._radius = radius
        self._color = color

    def get_radius(self):
        return self._radius
    
    def set_radius(self, new_radius):
        if isinstance(new_radius, float) and new_radius > 0:
            self._radius = new_radius
        else:
            print(new_radius, " is not a valid radius.")
    def get_color(self):
        return self._color;
    def set_color(self, new_color):
        if new_color in Circle.VALID_COLORS:
            self._color = new_color
        else:
            print("Please enter a valid color.")

    radius = property(get_radius, set_radius)
    color = property(get_color, set_color)

my_circle = Circle(10, "Blue")
print(my_circle.get_radius(), my_circle.get_color())
my_circle.set_radius(16.0)
my_circle.set_color("Pink")
print(my_circle.get_radius(), my_circle.get_color())
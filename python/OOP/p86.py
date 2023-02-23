class Circle:
    def __init__(self, radius) -> None:
        self._radius = radius

    def find_diameter(self):
        return self._radius * 2;

my_circle = Circle(5.4)
diameter = my_circle.find_diameter()
print(diameter)
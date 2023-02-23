class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius

    def find_diameter(self):
        print(f"Diameter: {self.radius * 2}")

my_circle = Circle(4)
my_circle.find_diameter()
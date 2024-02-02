# Part 1
# What does the following code do? Add a comment to each line of code
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        else:
            raise TypeError("Unsupported operand type for +: 'Circle' and {}".format(type(other)))

    def __str__(self):
        return f"Circle with radius {self.radius}"

# Examples
circle1 = Circle(5)
circle2 = Circle(3)
circle3 = Circle(8)

result_circle = circle1 + circle2
print(result_circle)  # Output: Circle with radius 8

result_circle = circle1 + circle3
print(result_circle)  # Output: Circle with radius 13

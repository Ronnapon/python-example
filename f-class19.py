# Data Class
from collections import namedtuple


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, point2):
        return self.x == point2.x and self.y == point2.y


point1 = Point(1, 2)
point2 = Point(1, 2)
# Format 1
print(id(point1))
print(id(point2))
print("Format1", point1 == point2)  # Output False Because Memory is not =
# ----------->
# Format 2
Point = namedtuple("Point", ["x", "y"])
point1 = Point(x=1, y=2)
point2 = Point(x=1, y=2)
# point1.x = "5" (Cannot do it)
print("Format2", point1 == point2)

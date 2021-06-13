# Class vs instance Attribute.
class Point:
    defual_corlor = "Red"  # Class Attibute

    def __init__(self, x, y):
        self.x = x  # instance Attribute
        self.y = y  # instance Attribute

    def draw(self):
        print(f"x = {self.x}, y = {self.y}")
        return "Good Bye"


print(Point.defual_corlor)
Point.defual_corlor = "Yellow"
# ----------------------->
print("*" * 25)
point1 = Point('a', 'b')
print(point1.defual_corlor)
print(point1.draw())
# ----------------------->
print("*" * 25)
point2 = Point('e', 'f')
print(point2.defual_corlor)
print(point2.draw())

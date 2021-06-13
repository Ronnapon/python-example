# Class instance vs Method
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod  # Class instance
    def zero(cls):
        return cls('a', 'b')

    def draw(self):
        print(f"x = {self.x} , y = {self.y}")
        return "Good Bye"


point = Point.zero()  # (Point('a','b')), Factory method
print(point.draw())

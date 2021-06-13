# Magic Method (https://rszalski.github.io/magicmethods/)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls('a', 'b')

    def __str__(self):
        return f"x = {self.x} , y = {self.y}"

    def draw(self):
        return "Good Bye"


point = Point.zero()  # (Point('a','b')), Factory method
print(point)  # Return Str from __str__
print(point.draw())

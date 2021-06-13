# Number Magic Method
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, point2):
        return Point(self.x + point2.x, self.y + point2.y)


point1 = Point(1, 3)
point2 = Point(2, 4)
combine = point1 + point2
print(combine.x)
print(combine.y)

# __add__(self, other)
# Implements addition.
# __sub__(self, other)
# Implements subtraction.
# __mul__(self, other)
# Implements multiplication.
# __floordiv__(self, other)
# Implements integer division using the // operator.
# __div__(self, other)
# Implements division using the / operator.
# __truediv__(self, other)
# Implements true division. Note that this only works when from __future__ import division is in effect.
# __mod__(self, other)
# Implements modulo using the % operator.
# __divmod__(self, other)
# Implements behavior for long division using the divmod() built in function.
# __pow__
# Implements behavior for exponents using the ** operator.
# __lshift__(self, other)
# Implements left bitwise shift using the << operator.
# __rshift__(self, other)
# Implements right bitwise shift using the >> operator.
# __and__(self, other)
# Implements bitwise and using the & operator.
# __or__(self, other)
# Implements bitwise or using the | operator.
# __xor__(self, other)
# Implements bitwise xor using the ^ operator.

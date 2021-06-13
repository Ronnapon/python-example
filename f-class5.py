# Comparetion magic Method
# Class vs instance Attribute.


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, point2):
        return self.x == point2.x and self.y == point2.y

    def draw(self):
        print(f"x = {self.x}, y = {self.y}")
        return "Good Bye"


point1 = Point('a', 'b')
point2 = Point('a', 'b')
print(point1 == point2)


# _cmp__(self, other)
# __cmp__ is the most basic of the comparison magic methods. It actually implements behavior for all of the comparison operators (<, ==, !=, etc.), but it might not do it the way you want (for example, if whether one instance was equal to another were determined by one criterion and and whether an instance is greater than another were determined by something else). __cmp__ should return a negative integer if self < other, zero if self == other, and positive if self > other. It's usually best to define each comparison you need rather than define them all at once, but __cmp__ can be a good way to save repetition and improve clarity when you need all comparisons implemented with similar criteria.
# __eq__(self, other)
# Defines behavior for the equality operator, ==.
# __ne__(self, other)
# Defines behavior for the inequality operator, !=.
# __lt__(self, other)
# Defines behavior for the less-than operator, <.
# __gt__(self, other)
# Defines behavior for the greater-than operator, >.
# __le__(self, other)
# Defines behavior for the less-than-or-equal-to operator, <=.
# __ge__(self, other)
# Defines behavior for the greater-than-or-equal-to operator, >=.

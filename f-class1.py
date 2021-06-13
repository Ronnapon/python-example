# Class is a blueprint for createing new object ,object is instance of a class, Class: Human, Object: Big, Aut, Pun,
# Class Constuctor


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"x = {self.x} , y = {self.y}, z = {self.z}")
        return "Good Bye"


point = Point('a', 'b')
point.z = 'c'
print(point.draw())

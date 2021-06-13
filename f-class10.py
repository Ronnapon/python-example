# inheritance
class Animal:
    def __init__(self):
        self.age = 5

    def eat(self):
        print("eat")


class Mammal(Animal):  # Parent Animal (Base), Child Malmal
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


mammal = Mammal()
mammal.eat()
print(mammal.age)

fish = Fish()
fish.eat()
print(fish.age)
print(isinstance(mammal, object))
print(issubclass(Mammal, object))

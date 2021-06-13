# Method Over riding
# inheritance


class Animal:
    def __init__(self):
        self.age = 5

    def eat(self):
        print("eat")


class Mammal(Animal):  # Parent Animal (Base), Child Malmal
    def __init__(self):  # Replace constactor of base class  (Call method over riding)
        super().__init__()  # Call Animall class method __init__
        self.weight = 50

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


mammal = Mammal()
print(mammal.age)  # super().__init__()
print(mammal.weight)

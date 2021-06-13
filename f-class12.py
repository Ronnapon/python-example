# Muti lever inherritance  (You should have lever 1 or 2 lever, It's okay)
class Animal:
    def eat(self):
        print("eat")


class Bird(Animal):  # Level 1
    def fly(self):
        print("fly")


class Chicken(Bird):  # Level 2
    pass


chicken = Chicken()
chicken.eat()
chicken.fly()

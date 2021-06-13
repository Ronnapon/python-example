# Mutiple inheritance
class Flyer:
    def fly(self):
        print("fly")
        pass


class Swimmer:
    def swim(self):
        print("swim")
        pass


class FlySwim(Flyer, Swimmer):
    pass


animal = FlySwim()
animal.fly()
animal.swim()

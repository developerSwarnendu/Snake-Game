class Animal:
    def __init__(self) -> None:
        self.eyes=2

    def breathe(self):
        print("Inhale,exhale")


class Fish(Animal): # in this way we can inherit the Animal class in the Fish class...
    def __init__(self) -> None:
        super().__init__ # by using this super() method we call the constructor of the super class...

    def move(self):
        print("Moves under water.")


fish=Fish()

fish.move()
fish.breathe()
from OOP.animals.animal import Animal


class Bird(Animal):

    def __init__(self):
        super().__init__()

    def fly(self, km, x):
        print("fly km: ", km, "and x is:", x)

    def make_bird_sound(self):
        super().make_sound("tweet tweet")

    def move(self):
        print("Bird move")

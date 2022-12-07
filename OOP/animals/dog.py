from OOP.animals.animal import Animal


class Dog(Animal):

    def __init__(self):
        super().__init__()

    def run(self, km):
        print("run km: ", str(km))

    def make_dog_sound(self):
        super().make_sound("Hav Hav")

    def move(self):
        print("dog move")

from abc import abstractmethod, ABC


class Animal(ABC, object):
    name = ""

    def __init__(self):
        self.time = 0

    def eat(self):
        print("eat")

    def sleep(self, time):
        print("sleep in hours: ", time)

    def make_sound(self, sound):
        print(sound)

    @abstractmethod
    def move(self):
        pass

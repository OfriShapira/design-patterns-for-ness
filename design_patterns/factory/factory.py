class Cola(object):
    def drink(self):
        print("drink cola")


class Sprite(object):
    def drink(self):
        print("drink sprite")


class Factory(object):
    def __init__(self, drink_name):
        self.drink_name = drink_name

    def get_object(self):
        if self.drink_name > 10:
            return Cola()
        else:
            return Sprite()

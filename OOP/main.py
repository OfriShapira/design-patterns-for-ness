from animals.bird import Bird
from animals.dog import Dog

if __name__ == '__main__':
    d = Dog()
    d.sleep(3)
    d.run(4)
    d.make_dog_sound()

    d = Bird()
    d.fly(30, 10)
    d.make_bird_sound()
    d.move()

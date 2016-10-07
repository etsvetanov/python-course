class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def make_sound(self):
        print('Bau')


class Sheep(Animal):
    def make_sound(self):
        print('Beeee')


class Parrot(Animal):
    def make_sound(self):
        print('I am a parrot')


sheep = Sheep('Doli')
dog = Dog('Sharo')
parrot = Parrot('Poli')

sheep.make_sound()
dog.make_sound()
parrot.make_sound()
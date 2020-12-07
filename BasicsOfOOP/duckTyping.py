
"""
duck typing allows users to implement functions  without worrying about
data type 

"""


class Cow:
    def speak(self):
        print('Moo Moo')

class Lion:
    def speak(self):
        print('Rooo Rooo')

class Cat:
    def speak(self):
        print('meoww meoww')

class AnimalSound:
    def sound(self,animal):
        animal.speak()

Sound=AnimalSound()

for animal in [Cow(),Lion(),Cat()]:
    Sound.sound(animal)
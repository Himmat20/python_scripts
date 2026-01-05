# Abstraction 
# hiding internal details and showing only essential features

from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound():
        pass

class Lion(Animal):
    def make_sound(self):
        print("sound is 'roar'")

class Cat(Animal):
    def make_sound(self):
        print("sound is 'meow'")

l1=Lion()
l1.make_sound()
c1=Cat()
c1.make_sound()

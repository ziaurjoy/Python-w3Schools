

from abc import ABC, abstractmethod

class Robot(ABC): # Abstract class
    @abstractmethod
    def show_name(self): # Abstract method
        pass

class Human(Robot):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_name(self):
        return self.name

    def show_age(self):
        return self.age

human1 = Human("Joy", 20)
print(human1.show_name())
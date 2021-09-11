

# class Robot:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show_name(self):
#         return self.name
#
#     def show_age(self):
#         return self.age
#
# class Human:
#     def __init__(self, name, age, food):
#         self.name = name
#         self.age = age
#         self.food = food
#
#     def show_name(self):
#         return self.name
#
#     def show_age(self):
#         return self.age
#
#     def show_food(self):
#         return self.food
#
# robot = Robot("Sufia", "Age 6" )
# human = Human("Joy", "Age 20", "Apple")
#
# print("-" * 5, "Robot", "-"*5)
# print(robot.show_name())
# print(robot.show_age())
#
# print("-" * 5, "Human", "-"*5)
# print(human.show_name())
# print(human.show_age())
# print(human.show_food())





# class Robot:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show_name(self):
#         return self.name
#
#     def show_age(self):
#         return self.age
#
# class Human(Robot):
#     def __init__(self, name, age, food):
#       super().__init__(name, age)
#       self.food = food
#
#     def show_food(self):
#         return self.food
#
# class Animal(Human):
#     def __init__(self, name, age, food, pet):
#         super().__init__(name, age, food)
#         self.pet = pet
#
#     def pet_type(self):
#         return self.pet
#
# animal = Animal("Pushi", "3 year's ", "milk", 'cat')
#
# robot = Robot("Sufia", "Age 6" )
# human = Human("Joy", "Age 20", "Apple")
#
# print("-" * 5, "Robot", "-"*5)
# print(robot.show_name())
# print(robot.show_age())
#
# print("-" * 5, "Human", "-"*5)
# print(human.show_name())
# print(human.show_age())
# print(human.show_food())
#
# print("-" * 5, "Animal", "-"*5)
# print(animal.show_name())
# print(animal.show_age())
# print(animal.show_food())
# print(animal.pet_type())





class Robot:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_name(self):
        return self.name

    def show_age(self):
        return self.age

class Human:
    def __init__(self, name, age, food):
      self.name = name
      self.age = age
      self.food = food

    def show_name(self):
        return self.name

    def show_age(self):
        return self.age

    def show_food(self):
        return self.food

class Animal(Robot, Human):
    def __init__(self, name, age, food, pet):
        Robot.__init__(self, name, age)
        Human.__init__(self, name, age, food)
        self.pet = pet

    def pet_type(self):
        return self.pet

animal = Animal("Pushi", "3 year's ", "milk", 'cat')

robot = Robot("Sufia", "Age 6" )
human = Human("Joy", "Age 20", "Apple")

print("-" * 5, "Robot", "-"*5)
print(robot.show_name())
print(robot.show_age())

print("-" * 5, "Human", "-"*5)
print(human.show_name())
print(human.show_age())
print(human.show_food())

print("-" * 5, "Animal", "-"*5)
print(animal.show_name())
print(animal.show_age())
print(animal.show_food())
print(animal.pet_type())



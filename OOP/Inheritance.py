
# Inheritance

# class Moster:
#     def __init__(self, heads, color):
#         self.heads = heads
#         self.color = color
#
#     def attack(self):
#         return "I am attacking"
#
# class Fogthing(Moster):
#     def make_sound(self):
#         return "GGGGrrrrrrr"
#
# class Mournsnake(Moster):
#     def make_sound(self):
#         return "Hiiisssssssh"
#
# obj1 = Mournsnake(4, "Black")
# obj2 = Fogthing(2, "Green")
#
# print(obj1.attack())
# print(obj1.make_sound())
#
# print(obj2.attack())
# print(obj2.make_sound())



# Multiple Inheritance

# class Moster:
#     def __init__(self, heads, color):
#         self.heads = heads
#         self.color = color
#
#     def attack(self):
#         return "I am attacking"
#
# class Fogthing(Moster):
#     def make_sound(self):
#         return "GGGGrrrrrrr"
#
# class Mournsnake(Moster):
#     def make_sound(self):
#         return "Hiiisssssssh"
#
# class MultipleInheritance(Mournsnake, Fogthing):
#     pass
#
# obj1 = MultipleInheritance(4, "Black")
# print(obj1.make_sound())


class A:
    def spam(self):
        print(1)

class B(A):
    def spam(self):
        print(2)
        # super().spam()

B().spam()


# class Moster:
#     _identity = "Hello I am Hero" # attibute
#     def __init__(self, heads, color):
#         self.heads = heads
#         self.color = color
#     def _attack(self):
#         return "Attack Him"
#
# obj1 = Moster(4, "Black")
# obj2 = Moster(3, "Read")
#
# print(obj1.heads, "and", obj1.color, obj1._attack(), obj1._identity)
# print(obj2.heads, "and", obj2.color, obj2._identity)
#
#
#
# class Moster:
#     __identity = "Hello I am Hero" # __ strong private
#     def __init__(self, heads, color):
#         self.heads = heads
#         self.color = color
#     def __attack(self): # __ strong private
#         return "Attack Him"
#
# obj1 = Moster(4, "Black")
# obj2 = Moster(3, "Read")
#
# print(obj1.heads, "and", obj1.color, obj1.__attack(), obj1.__identity)
# print(obj2.heads, "and", obj2.color, obj2.__identity)



class Moster:
    __identity = "Hello I am Hero" # __ strong private
    def __init__(self, heads, color):
        self.heads = heads
        self.color = color
    def attack(self):
        return self.__identity # accessing private attibute

obj1 = Moster(4, "Black")
obj2 = Moster(3, "Read")

print(obj1.heads, "and", obj1.color, obj1.attack())
# print(obj2.heads, "and", obj2.color, obj2.__identity)
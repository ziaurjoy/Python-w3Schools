# class Moster:
#     def __init__(self, heads, color):
#         self.heads = heads
#         self.color = color
#
# obj1 = Moster(4, "Black")
# obj2 = Moster(3, "Read")
# obj3 = Moster(2, "Green")
#
# print(obj1.heads, "and", obj1.color)
# print(obj2.heads, "and", obj2.color)




class Moster:
    identity = "Hello I am Hero" # attibute
    def __init__(self, heads, color):
        self.heads = heads
        self.color = color
    def attack(self):
        return "Attack Him"

obj1 = Moster(4, "Black")
obj2 = Moster(3, "Read")

print(obj1.heads, "and", obj1.color, obj1.attack(), obj1.identity)
print(obj2.heads, "and", obj2.color, obj2.identity)
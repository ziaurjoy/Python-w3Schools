

# class Persion:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def print_name(self):
#         return self.first_name + self.last_name
#
# p1 = Persion("Ziaur Rahman ","Joy")
# print(p1.print_name())
#
# class Student(Persion):
#     pass
# p2 = Student("Joy ", "Bangladesh")
# print(p2.print_name())


#
# class Persion:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def print_name(self):
#         return self.first_name + self.last_name
#
# class PersionExtra(Persion):
#     def __init__(self, first_name, last_name, age):
#         Persion.__init__(self, first_name, last_name)
#         self.age = age
#
#     def print_all(self):
#         return self.first_name + self.last_name, self.age
#
# p1 = PersionExtra("Bangladesh ", "JOy ",20)
# print(p1.print_all())





# class Persion:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def print_name(self):
#         return self.first_name + self.last_name
#
# class Student(Persion):
#     def __init__(self, first_name, last_name, age):
#         #super().__init__(first_name, last_name)
#         Persion.__init__(self, first_name, last_name)
#         self.age = age
#
#     def print_name(self):
#         return self.first_name + self.last_name + str(self.age)
#
# s1 = Student("Ziaur Rahman ", "Joy ", 20)
# print(s1.print_name())


# class MyNumber:
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x
#
# my_class = MyNumber()
# my_iter = iter(my_class)
#
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))


# class MyNumber:
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise
#
# my_class = MyNumber()
# my_iter = iter(my_class)
# for i in my_iter:
#     print(i)







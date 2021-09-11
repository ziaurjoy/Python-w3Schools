



# def decorator(func):
#     def decorate():
#         print("---------------")
#         func()
#         print("---------------")
#     return decorate
#
# def print_test():
#     print("Hello Bangladesh")
#
# print_test()
# my_decorator = decorator(print_test)
# my_decorator()




def decorator(func):
    def decorate(name):
        print("---------------")
        func(name)
        print("---------------")
    return decorate

@decorator
def hello(name):
    print(name)


print(hello("Bangladesh"))
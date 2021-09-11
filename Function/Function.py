

# def my_function():
#     print("Hello I am Joy")
#
# my_function()
#
# def my_function(name):
#     print("Hello, ", name)
# my_function("Joy")
#
# def my_function(name):
#     print(f"Hello, {name}")
# my_function("Joy")
#
#
# def my_function(*name):
#     for i in range(len(name)):
#         print("Hello,", name[i])
# my_function("Joy", 'Ziaur', 'Bangladesh')



# def my_function(**name):
#     print(name)
# my_function(a = "Joy", b= 'Ziaur', c='Bangladesh')


# def my_function(*name):
#     print(name)
# my_function(a = "Joy", b= 'Ziaur', c='Bangladesh')

# def name(name):
#     return name
#
# def age(age, name):
#     return "name is", name, "and", age
#
# print(age(20, name("Joy")))
#
#
# def my_function(**kid):
#   print("His last name is " + kid["lname"])
# my_function(fname = "Tobias", lname = "Refsnes")



# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result
#
# print("\n\nRecursion Example Results")
# tri_recursion(6)

# def recursion(k):
#     if k > 0:
#         result = k+recursion(k-1)
#         print(result)
#     else:
#         result = 0
#     return result
#
# recursion(6)


def number_duble(number):
    return number * 2

list1 = [10, 20, 30, 40]
result = map(number_duble, list1)
print(list(result))


def number_filter(number):
        return number % 2 == 0

list1 = [15, 20, 33, 40]
result = filter(number_filter, list1)
print(list(result))


list1 = [10, 20, 30, 40]
result = list(map(lambda x: x*2, list1))
print(result)

list1 = [15, 20, 33, 40]
result = list(filter(lambda x: x % 2 == 0, list1))
print(result)

# x = lambda a : a+5
# print(x(5))
#
# x = lambda a,b,c: a+b+c
# print(x(1,2,3))
#
#
# def my_func(n):
#     return lambda a: n*a
#
# fun = my_func(10)
#
# print(fun(2))

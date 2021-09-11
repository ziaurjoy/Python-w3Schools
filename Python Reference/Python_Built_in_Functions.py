
# abs
a = 10.6
print(abs(a))

a = 3+5j
print(abs(a))


# all
mylist = [True, True, True]
x = all(mylist)
print(x)

mylist = [False, False, False]
x = all(mylist)
print(x)

mylist = [0, 1, 1]
x = all(mylist)
print(x)
# Returns False because 0 is the same as False



# return any true
mylist = [False, True, False]
x = any(mylist)
print(x)


# binary number
x = 10
print(bin(x))


def x():
  a = 5
print(callable(x))



x = chr(98)
print(x)



x = memoryview(b"Hello")
print(x)



a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")
x = zip(a, b)
#use the tuple() function to display a readable version of the result:
print(tuple(x))
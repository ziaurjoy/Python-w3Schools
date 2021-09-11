

"""
Global Variables:
    Variables that are created outside of a function (as in all of the examples above) are known as global variables.
    Global variables can be used by everyone, both inside of functions and outside.
"""
"""
x = 10 # Global Variable

def myFunc():
    print("My number is ", x) # Useing Global function

myFunc() # function Diclaration


def myFunction():
    y = 20
    print("Two number are x and y ", x, y)

myFunction()
print("Number of x is ", x) #global variable useing
# print("Number of y is ", y) # error but local variable not useing

"""

# The global Keyword
x = 10
def myFunction():
    global y
    y = 20
    print("Two number are x and y ", x, y)
myFunction()
print("Number of x is ", x) #global variable useing
print("Number of y is ", y)


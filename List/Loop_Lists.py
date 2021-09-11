

# thislist = ["apple", "banana", "cherry"]
# for i in thislist:
#     print(i)
#
# for i in range(len(thislist)):
#     print(i)
"""

i = 0
while i < len(thislist):
    print(i)
    i += 1

# List Comprehension
[print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for i in fruits:
    if "a" in i:
        newlist.append(i)
print(newlist)

newlist = [i for i in fruits if "a" in i]
print(newlist)

newlist = [i for i in fruits if i != "apple"]
print(newlist)

newlist = [i for i in fruits]
print(newlist)

newlist = [i for i in range(10)]
print(newlist)

newlist = [i.upper() for i in fruits]
print(newlist)

newlist = ['hello' for x in fruits]
print(newlist)

"""

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
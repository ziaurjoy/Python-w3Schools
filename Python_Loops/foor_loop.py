fruits = ["apple", "banana", "cherry"]
# for i in fruits:
#     print(i)
#
# country = "Bangladesh"
# for i in country:
#     print(i)


# break statement
fruits = ["apple", "banana", "cherry"]
for i in fruits:
    if i == "banana":
        break
    else:
        print(i)

# continue statement
fruits = ["apple", "banana", "cherry"]
for i in fruits:
    if i == "banana":
        continue
    else:
        print(i)

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for i in adj:
    for j in fruits:
        print(i, j)
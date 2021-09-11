

this_set = {"Bangladesh", "India", "Pakistan"}
print(this_set)

this_set = {"Bangladesh", "India", "Pakistan", "India", "Bangladesh"}
print(this_set)

# length
print(len(this_set))

# Set item data type

number = {1, 2, 3, 4, 5}
string = {"Bangladesh", "India", "Pakistan"}
boolean = {True, False, True, True}
print(number, string, boolean)


persion = {"Joy", 30, True}
print(persion)

# convert set
this_set = set(("Joy", 30, True))
print(this_set)




# Access in set

this_set = {"apple", "banana", "charry"}

for i in this_set:
    print(i)

print("banana" in this_set)


# add in set

this_set = {"apple", "banana", "charry"}
this_set.add("mango")
print(this_set)

country = {"Bangladesh", "India", "Pakistan"}
city = {"Dhaka", "Dilli", "Islamabad"}
country.update(city)
print(country)

country = {"Bangladesh", "India", "Pakistan"}
city = ["Dhaka", "Dilli", "Islamabad"]
country.update(city)
print(country)


# remove
country = {"Bangladesh", "India", "Pakistan"}
country.remove("India")
print(country)
print("India" in country)


country = {"Bangladesh", "India", "Pakistan"}
# country.discard("India")
# print(country)
# print("India" in country)
#
# x = country.pop()
# print(x)
#
# x = country.clear()
# print(x)

# del country
# print(country)


# Join Set

set1 = {"a", "b", "c"}
set2 = {1, 2, 3, 4, 5, "c"}
set3 = set1.union(set2)
print(set3)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection(y)
print(x)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference(y)
print(x)


persion = {
    "Name": "Ziaur Rahman Joy",
    "age": 20,
    "District": "Bogura"
}
print(persion)
print(persion["Name"])



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)


thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
print(thisdict["colors"][0])


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# x = thisdict["model"]
x = thisdict.get("model")
print(x)
y = thisdict.keys()
print(y)



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

thisdict["colors"] = "Red"

print(thisdict)
print(thisdict.values())
print(thisdict.items())


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)

# thisdict.pop("brand")
print(thisdict)

print(thisdict.popitem())


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict:
  print(x)

for x in thisdict.values():
  print(x)

for keys, values in thisdict.items():
    print(keys, values)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

my_family = {
    "children1": {
        "Name": "Joy",
        "Age": 20
    },
    "children2": {
            "Name": "Ziaur",
            "Age": 23
        },
    "children3": {
            "Name": "Bangladesh",
            "Age": 50
        }
}

print(my_family["children1"]["Age"])


child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily["child1"])


age = 20
txt = "My age is ", 20
print(txt)

text = "My age is {}".format(20)
print(text)

text2 = f"My age is {20}"
print(text2)


quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

myorder = "I want {} pieces of item {} for {} dollars.".format(quantity, itemno, price)
print(myorder)

myorder = f"I want {quantity} pieces of item {itemno} for {price} dollars."
print(myorder)
# class Rectangle:
#     def __init__(self, height, width):
#         self.height = height
#         self.width = width
#
#     def calculate_area(self):
#         return self.width * self.height
#
#     @classmethod
#     def new_squre(cls, a, b):
#         return cls(a, b)
#
# obj1 = Rectangle(10, 20)
# print(obj1.calculate_area())
#
# obj2 = Rectangle.new_squre(5, 10)
# print(obj2.calculate_area())





class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples!")
        else:
            return True

ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)














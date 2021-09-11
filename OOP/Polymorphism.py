

class Robot:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_name(self):
        return self.name

    def show_age(self):
        return self.age

class Human(Robot):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #Mthod Overiding
    def show_name(self):
        return self.name

    def show_age(self):
        return self.age

robot1 = Robot("Sofia", 5)
human1 = Human("Joy", 20)
# print(robot1.show_name())
# print(human1.show_name())

for obj in [robot1, human1]:
    print(obj.show_name())




class Profile:
    # method overlodding
    def name(self, first_name = None, middle_name = None, last_name = None):
        if first_name != None and middle_name != None and last_name != None:
            return first_name+' '+middle_name+' '+last_name
        if first_name != None and middle_name != None:
            return first_name+' '+middle_name
        if first_name != None:
            return first_name

persion1 = Profile()
print(persion1.name("Ziaur", "Rahman", "Joy"))

persion2 = Profile()
print(persion2.name("Ziaur", "Rahman"))

persion3 = Profile()
print(persion3.name("Ziaur"))
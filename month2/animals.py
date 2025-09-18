"""
dog class
"""
class Dog:
    # constructor
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    #method - woof woof - bark
    def bark(self):
        print("woof woof")
    
"""
cat class
"""
class Cat:
    # constructor
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    # def detring():
    #     pass
    def meow(self):
        print("meow meow")

    def printName(self):
        print(self.name)
    def __str__(self):
        print(self.name)
        return "this class requires a name and breed\majesty"
        
        
# myDog = Dog("sparky", "mastiff")
# myDog.bark()

myCat = Cat("tiger", "lion")
myCat.name = "alcatraz"
# del myCat.breed
# myCat.meow()
# myCat.printName()
myCat.printName()
print(myCat.breed)


"""
a human class that have properties of no of eyes, hair color, gender and height
"""
class Human:
    def __init__(self, eyes, hair_color, legs, gender, height):
        self.eyes = eyes
        self.hair_color = hair_color
        self.legs = legs
        self.gender = gender
        self.height = height

    def walking(self):
        print("I am walking")

    def speaking(self):
        print("I am talking")

    def breathing(self):
        print("I am  breathing")

person = Human(2, "black", 2, "female", "5.5ft")
person.walking()
person.speaking()
person.breathing()
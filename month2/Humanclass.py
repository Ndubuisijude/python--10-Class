"""
human class
constructor - name, five senses, limbs, skin tone, height
methods -walking, talking
"""

class Human:
    def __init__(self, name, eyes, ears, nose, tongue, skin, limbs, skinTone, height):
        self.name = name
        self.eyes = eyes
        self.ears = ears
        self.nose = nose
        self.tongue = tongue
        self.skin = skin
        self.limbs = limbs
        self.skinTone = skinTone
        self.height = height
    def walking(self):
        print(f"{self.name} am walking")
    def talking(self):
        print(f"{self.name} am talking")

majesty = Human("Majesty", 2,2, 1, 1,"feeling",4, "dark", "6.1ft")
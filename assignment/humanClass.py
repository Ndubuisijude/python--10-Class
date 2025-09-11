"""
a human class that have properties of no of eyes, hair color, gender and height
"""
class Human:
    def _init_(self, no_of_eyes: int, hair_color: str, no_of_legs: int, gender: str, height: float):
        try:
            if not (isinstance(no_of_eyes, int) and no_of_eyes >= 0): raise ValueError("Invalid eyes")
            if not isinstance(hair_color, str): raise ValueError("Invalid hair color")
            if not (isinstance(no_of_legs, int) and no_of_legs >= 0): raise ValueError("Invalid legs")
            if not isinstance(gender, str): raise ValueError("Invalid gender")
            if not (isinstance(height, (int, float)) and height > 0): raise ValueError("Invalid height")
            
            self.no_of_eyes, self.hair_color, self.no_of_legs, self.gender, self.height = no_of_eyes, hair_color, no_of_legs, gender, height
        except ValueError as e:
            print(f"Error: {e}")
            raise

    def walking(self): print("I am walking")
    def speaking(self): print("I am talking")
    def breathing(self): print("I am breathing")


# Example usage
if __name__ == "__main__":
    try:
        person = Human(2, "brown", 2, "male", 5.8)
        person.walking()
        person.speaking()
        person.breathing()
    except ValueError as e:
        print(f"Error: {e}")

"""
Having Aptech as your starting point, directing a user either of two locations: Abakpa or Emene.
"""

 # get user input for direction
name = input("please enter your name: ") 
direction = input("please enter your direction (Abakpa or Emene): ").strip().lower()

# Function to get directions
def get_directions(name, direction):
    print(f"\nHello, {name}! here are your directions from Aptech in Enugu:")
    if direction == "abakpa":
        print("To get to Abakpa from Aptech:")
        print("1. Head west from Aptech towards the main road (likely Ogui Road or nearby major road).")
        print("2. Continue straight until you reach the Abakpa Nike Junction.")
        print("3. At the Abakpa Nike Junction, take a slight right onto Abakpa Nike road.")
        print("4. proceed along Abakpa Nike road for approximately 2-3 km")
        print("5. You will arrive in Abakpa, near the Abakpa Market or Abakpa-Nike Junction.")

    elif direction == "emene":
        print("To get to Emene from Aptech:")
        print("1. Head east from Aptech towards Enugu-Port Harcourt Expressway.")
        print("2. Merge onto the Enugu-Port Harcourt Expressway heading towards Emene.")
        print("3. Continue for about 5-7 km, passing the New Artisan Market.")
        print("4. Look for signs for Emene or the Nike Lake-Harmony Estate-Adoration Ministry road.")
        print("5. Turn left onto the Nike Lake-Harmony Estate-Emene road to enter Emene.")
        print("6. You will arrive in Emene, near landmarks like the Eke-Obinagu Junction.")

    else:
        print("Invalid direction! Please enter either \"Abakpa\" or \"Emene\".")

# call the function with user inputs
get_directions(name, direction)


#  Assignment 2
"""
build a game called odd or even that will ask a user for a number and then tell them if the number is odd or even.
# """
def odd_or_even():
    try:
        # Ask user for a number
        number = int(input("Please enter a number: "))
        
        # Check if number is even or odd
        if number % 2 == 0:
            print(f"{number} is even!")
        else:
            print(f"{number} is odd!")
            
    except ValueError:
        print("Please enter a valid integer!")

# Run the game
odd_or_even()


# Assignment 3
"""
building a simple password checker
"""
password = input("Enter password: ")

if password == "MR FRANK":
    print("Access given")
else:
    print("Access denied")


# Assignment 4
"""
simple program that takes two numbers as input from the user and outputs the greater number
"""

# Get user input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# compare the numbers and find the greater number
if num1 > num2:
    print(f"The greater number is: {num1}")
elif num2 > num1:
    print(f"The greater number is: {num2}")
else:
    print("Both numbers are equal.")

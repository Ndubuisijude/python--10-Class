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
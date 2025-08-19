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

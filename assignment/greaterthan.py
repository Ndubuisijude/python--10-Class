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


# class learning on greater than
"""
get two int input and return the greater
"""
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))

if(num1 == num2):
    print("the numbers are the same")
elif (num1 < num2):
    print(f"num2: {num2} is the greater number" )
else:
    print(f"num1: {num1} is the greater")



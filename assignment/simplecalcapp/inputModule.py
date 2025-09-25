"""
This  module handles user input for the application.
"""
def num1(): 
  return int(input("input your first number: "))
def num2():
    return int(input("enter your second number: "))

    #operation input
def op():
    return input("enter your operation: add \nsub \nmult \ndiv ").lower()
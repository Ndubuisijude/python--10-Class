""" 
build a simple fizzbuzz program that prints 1 to 30 while 3 or any number divisible by 3 it should print out the word "fizz" if it gets to a number 5 or divisible by 5 it should print out the word "buzz"
"""
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
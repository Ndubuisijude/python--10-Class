"""

Wrap up the entire simplecalc.py project in a while loop.

After the program runs, it should ask the user if he/she wants to continue with the program . If yes, the program should run again.
If no, the program should stop running
"""

while True:
# user inputs, num1 and num2
 num1 = int(input("enter your first number: "))
 num2 = int(input("enter your second number: "))

#operation input
 op = input("enter your operation: sum \n difference \n quotient \n product \n ").lower()

#sum, difference, quotient, product
 def addition():
    sum = num1 + num2
    print(f"this is the sum: {sum}")

 def difference():
    difference= num1 - num2
    print(f"this is the difference of two numbers: {difference}")

 def divide():
    quotient = num1 / num2
    print(f"this is the quotient of two numbers: {quotient}")

 def multiply():
    product = num1 * num2
    print(f"this is the product of two numbers: {product}")


#user choice-input

 choice = input("do you want to continue: enter any key to continue or no to stop?")

# condition statements
 if (op.lower() == "sum"):
    addition()
 elif (op.lower() == "difference"):
    difference()
 elif (op.lower() == "quotient"):
    if (num2 == 0):
        print("undefined")
    else:
        divide()
 elif (op.lower() == "product"):
    multiply()
 else:
   print("invalid operation")
   continue
 print("end of program")
 if choice.lower() == "no":
        break
"""
will ask a user to select the sum, quotient, product, difference of two numbers and then calculate the 
selected option which is being selected
"""

def calculator():
    print("select an operation")
    print("1. Sum (+)")
    print("2. Difference (-)")
    print("3. Product (*)")
    print("4. Quotient (/)")

    # get user input for operation
    choice = input("Enter choice (1-4): ")

    # Validate operation choice
    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice! Please select 1, 2, 3, or 4.")
        return

    # Get two numbers from the user
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
        return

    # Perform the selected operation
    if choice == '1':
        result = num1 + num2
        operation = '+'
    elif choice == '2':
        result = num1 - num2
        operation = '-'
    elif choice == '3':
        result = num1 * num2
        operation = '*'
    elif choice == '4':
        if num2 == 0:
            print("Error: Division by zero is not allowed!")
            return
        result = num1 / num2
        operation = '/'

    # Display the result
    print(f"{num1} {operation} {num2} = {result}")

# Run the calculator
calculator()

# correction on if statements / assignment 2

"""
simple calculator, that gets two user int inputs and operation returns sum, diff, quotient, product
"""

# user inputs, num1 and num2
num1 = int(input("enter your first number: "))
num2 = int(input("enter your second number: "))

#operation input
op = input("enter your operation: sum \n difference \n quotient \n product \n ").lower()

#sum, difference, quotient, product
sum = num1 + num2
difference= num1 - num2
quotient = num1 / num2 
product = num1 * num2

# condition statements

if (op.lower() == "sum"):
    print(f"this is the sum: {sum}")
elif (op.lower() == "difference"):
    print(f"this is the difference of two numbers: {difference}")
elif (op.lower() == "quotient"):
    if (num2 == 0):
        print("undefined")
    else:
        print(f"this is the quotient of two numbers: {quotient}")
elif (op.lower() == "product"):
    print(f"this is the product of two numbers: {product}")
else:
    print("invalid operation")

print("end of program")




# user inputs, num1 and num2
num1 = int(input("enter your first number: "))
num2 = int(input("enter your second number: "))

#operation input
op = input("enter your operation: sum \n difference \n quotient \n product \n ").lower()

#sum, difference, quotient, product
sum = num1 + num2
difference= num1 - num2
quotient = num1 / num2 
product = num1 * num2

# condition statements

if (op.lower() == "sum"):
    print(f"this is the sum: {sum}")
elif (op.lower() == "difference"):
    print(f"this is the difference of two numbers: {difference}")
elif (op.lower() == "quotient"):
    print(f"this is the quotient of two numbers: {quotient}")
elif (op.lower() == "product"):
    print(f"this is the product of two numbers: {product}")
else:
    print("invalid operation")

print("end of program")
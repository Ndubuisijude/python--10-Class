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

    

"""
making a program that will collect an int input from the user and check if it is positive
"""
while True:
    user_input = int(input("Enter a positive integer (negative to stop): "))
    if user_input < 0:
        print("Negative number entered. Program stopped.")
        break
    print(f"You entered: {user_input}")
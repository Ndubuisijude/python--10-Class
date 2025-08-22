"""
guess a number by setting a secret number and asking the user to guess it if correct you won
"""

secret_number = 8
guess = int(input("Enter your guess (1-10): "))
if guess == secret_number:
    print("Congratulations! You guessed the right number.")
else:
    print("Sorry, that's not correct. The secret number was", secret_number)
"""
A Simple ATM Simulator

Start with a balance of $1000
Ask user what they want to do: check balance, deposit, or withdraw
For deposits: add amount to balance
For withdrawals: check if sufficient funds exist
Display appropriate messages and updated balance
for this one
it will also be a console app
just like everything else
the atm simulator should look something like this
ATM Menu:
1. Check Balance
2. Deposit
3. Withdraw
Choose an option: 3
Enter withdrawal amount: $150
Transaction successful! New balance: $850
"""

def atm_simulator():
    balance = 1000  # Initial balance
    
    while True:
        # Display ATM menu
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        # Get user choice
        choice = input("Choose an option: ")
        
        # Check Balance
        if choice == "1":
            print(f"Your balance is: ${balance}")
        
        # Deposit
        elif choice == "2":
            try:
                amount = float(input("Enter deposit amount: $"))
                if amount > 0:
                    balance += amount
                    print(f"Deposit successful! New balance: ${balance}")
                else:
                    print("Please enter a positive amount.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        # Withdraw
        elif choice == "3":
            try:
                amount = float(input("Enter withdrawal amount: $"))
                if amount > 0:
                    if amount <= balance:
                        balance -= amount
                        print(f"Transaction successful! New balance: ${balance}")
                    else:
                        print("Insufficient funds!")
                else:
                    print("Please enter a positive amount.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        # Exit
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        
        # Invalid option
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")

# Run the ATM simulator
if __name__ == "__main__":
    atm_simulator()

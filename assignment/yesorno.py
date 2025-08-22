"""
build a program that asks the user a yes or no question and responds accordingly
"""
while True:
    cont = input("Do you want to continue? (yes/no): ").lower()
    if cont == "yes":
        continue
    elif cont == "no":
        break

# correctiion
"""
simple yes or no program
"""
#user choice-input

choice = input("do you want to continue: enter any key to continue or no to stop?")

#loop
while(choice == "y"):
    print("alright continuing the program")
    choice = input("do you want to continue: y or no?")
    if(choice == "y"):
        continue
    elif(choice == "n"):
        break
    else:
        print("invalid input")

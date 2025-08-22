"""
build a program that asks the user a yes or no question and responds accordingly
"""
while True:
    cont = input("Do you want to continue? (yes/no): ").lower()
    if cont == "yes":
        continue
    elif cont == "no":
        break

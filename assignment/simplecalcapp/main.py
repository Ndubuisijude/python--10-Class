"""
This module handles all user input complete"""
 #main.py
import inputModule
import logicModule

while True:  # this part makes the entire calculator run over and over again until its break by the user
    num1 = inputModule.num1()
    num2 = inputModule.num2()
    op = inputModule.op()

    result = logicModule.checkOp(op, num1, num2)
    # print("Result:", result)

    again = input("Do you want to continue? (yes/no): ").lower()
    if again != "yes":
        break
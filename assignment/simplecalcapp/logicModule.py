""" this is a code to check the operation and call the appropriate function 
"""

# logicModule.py
import functionsModule   

def checkOp(op, num1, num2):
    if op == "add":
       return   functionsModule.add(num1, num2)
    elif op == "sub":
        return functionsModule.sub(num1, num2)
    elif op == "mult":
        return functionsModule.mult(num1, num2)
    elif op == "div":
        return functionsModule.div(num1, num2)
    else:
        return "Invalid operation!"
import math
from myModule import repeat

def calc():
    expression = input("Operations can use [+ - * / ^ //]\n"
                       + "Enter the mathmatical expression (example: 2 + 3)\n" 
                       + "'pleas enter spaces between numbers and operations': ").split(" ")
    if len(expression) == 3:
        if expression[0].isnumeric() and expression[2].isnumeric():
            if expression[1] == "+":
                print(float(expression[0]) + float(expression[2]))
            elif expression[1] == "-":
                print(float(expression[0]) - float(expression[2]))
            elif expression[1] == "*":
                print(float(expression[0]) * float(expression[2]))
            elif expression[1] == "/":
                print(float(expression[0]) / float(expression[2]))
            elif expression[1] == "^":
                print(float(expression[0]) ** float(expression[2]))
            elif expression[1] == "//":
                print(float(expression[0]) // float(expression[2]))
            else: 
                print("Operation is not included")
        else: 
                print("Expression is not correct")
    print("Expression is not correct (dont forget spaces)")

repeat(calc)
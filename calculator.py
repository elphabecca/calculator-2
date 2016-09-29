"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic1 import *


# Your code goes here
def calc2():
    """Calculates numbers and operations in a specific format"""

    command = raw_input("> ")
    booger = "can't read, try +, -, *, /, square, cube, pow, or mod."
    while command != "q":
        tokens = command.split(" ")
        operand = tokens[0]
        symbol = ["+","-","*","/","square","cube","pow","mod"]
        
        if operand in symbol:
            if operand == "square" or operand == "cube":
                num1 = int(tokens[1])
                if operand == "square":
                    print square(num1)
                elif operand == "cube":
                    print cube(num1)
                else:
                    print booger

            elif operand == "/" or operand == "pow" or operand == "mod":
                num1 = int(tokens[1])
                num2 = int(tokens[2])
                if operand == "/":
                    print divide(num1, num2)
                elif operand == "pow":
                    print power(num1, num2)
                elif operand == "mod":
                    print mod(num1, num2)
                else:
                    print booger

            elif operand == "+" or operand == "-" or operand == "*":
                values = tokens[1:]
                if operand == "+":
                    print add(values)
                elif operand == "-":
                    print subtract(values)
                elif operand == "*":
                    print multiply(values)
                else:
                    print booger

        else:
            print booger
        command = raw_input("> ")

calc2()

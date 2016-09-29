"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
def calc2():
    """Calculates numbers and operations in a specific format"""

    command = raw_input("> ")
    print "I'm here!!!" + command
    while command != "q":
        tokens = command.split(" ")
        operand = tokens[0]
        if len(tokens) == 2:
            num1 = int(tokens[1])
            if operand == "square":
                print square(num1)
            elif operand == "cube":
                print cube(num1)
            else:
                print "can't read, try +, -, *, /, square, cube, pow, or mod."
        elif len(tokens) == 3:
            num1 = int(tokens[1])
            num2 = int(tokens[2])
            if operand == "+":
                print add(num1, num2)
            elif operand == "-":
                print subtract(num1, num2)
            elif operand == "*":
                print multiply(num1, num2)
            elif operand == "/":
                print divide(num1, num2)
            elif operand == "pow":
                print power(num1, num2)
            elif operand == "mod":
                print mod(num1, num2)
            else:
                print "can't read, try +, -, *, /, square, cube, pow, or mod."
        else:
            print "can't read, try +, -, *, /, square, cube, pow, or mod."
        command = raw_input("> ")

calc2()
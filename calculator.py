"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
def calc2(input):
    """Calculates numbers and operations in a specific format"""
    
    command = raw_input("> ")
    while command != "q":
        tokens = input.split(" ")
        if tokens[0] == "+":
            add(tokens[1], tokens[2])
        elif tokens[0] == "-":
            subtract(tokens[1], tokens[2])
        elif tokens[0] == "*":
            multiply(tokens[1], tokens[2])
        elif tokens[0] == "/":
            divide(tokens[1], tokens[2])
        elif tokens[0] == "square":
            square(tokens[1])
        elif tokens[0] == "cube":
            cube(tokens[1])
        elif tokens[0] == "pow":
            power(tokens[1], tokens[2])
        elif tokens[0] == "mod":
            mod(tokens[1], tokens[2])
        else:
            print "can't read, try +, -, *, /, square, cube, pow, or mod."
            calc2()
def add(num1, num2):
    return num1 + num2

def add_moar(*num):
    sum = 0
    numb = str(num).split(",")
    for num in numb:
        sum+=int(num)
        numb = numb[1:len(num)-1]
    return sum

add_moar(5,4,3,2,1)

def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    # Need to turn at least argument to float for division to
    # not be integer division
    return float(num1) / float(num2) 


def square(num1):
    # Needs only one argument
    return num1 * num1


def cube(num1):
    # Needs only one argument
    return num1 * num1 * num1


def power(num1, num2):
    return num1 ** num2  # ** = exponent operator


def mod(num1, num2):
    return num1 % num2


def add(values):
    sum_all = 0
    for nums in values:
        sum_all += int(nums)
    return sum_all

def subtract(values):
    sum_all = values[0]
    for nums in values[1:]:
        sum_all -= int(nums)
    return sum_all

def multiply(values):
    sum_all = 1
    for nums in values:
        sum_all *= int(nums)
    return sum_all

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

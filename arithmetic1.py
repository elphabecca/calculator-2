
def add(*nums):
    sum_all = nums[0]
    for num in nums[1:]:
        sum_all += num
    return sum_all

def subtract(*nums):
    difference = nums[0]
    for num in nums[1:]:
        difference -= num
    return difference

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

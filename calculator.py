# https://github.com/DRW2007/lab11-DW-JB.git
# Partner 1: Daniel Wagner
# Partner 2:
import math


def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)


def hypotenuse(a, b):
    return math.hypot(a, b)


def add(a, b): 
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Can't divide by zero!")
    return b / a


def log(a, b):
    try:
        return math.log(b, a)
    except ValueError:
        raise


def exp(a, b):
    pow(a, b)

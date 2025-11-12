<<<<<<< HEAD
import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example

def add(a, b): 
    return a + b

def sub(a, b): 
    a - b

def mul(a, b):
    return a * b

def div(a, b): 
    if a == 0:
        raise(ZeroDivisionError)
    else:
        return b / a
    
def log(a, b): 
    try: 
        log(b,a)# use math library + raise ValueError
    except:
        raise(ValueError)
    

def exp(a, b):
    return a ** b 


# https://github.com/DRW2007/lab11-DW-JB.git
# Partner 1: Daniel Wagner
# Partner 2: Jacobo Belilty
import math


def add(a, b): 
    return a + b



def sub(a, b):
    return a - b


def mul(a, b):
    return a * b




def log(a, b):
    try:
        return math.log(b, a)
    except ValueError:
        raise


def exp(a, b):
    pow(a, b)

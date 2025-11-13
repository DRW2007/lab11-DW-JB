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

def div(a, b): 
    if a == 0:
        raise(ZeroDivisionError)
    else:
        return b / a
    
def log(a, b): 
    try: 
        return log(b,a)# use math library + raise ValueError
    except:
        raise(ValueError)
    

def exp(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)


def hypotenuse(a, b):
    return math.hypot(a, b)

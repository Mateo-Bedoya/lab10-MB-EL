"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
<<<<<<< HEAD
def square_root(a):
    try:
        return math.sqrt(a)
    except a < 0:
        raise ValueError

def hypotenuse(a,b):
    return math.hypot(a,b)
# First example
=======

>>>>>>> 1c19d60da494e3d3590403f61db6666c27fa9275
def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")


def exp(a, b):
    return a ** b

# First example
def add(a, b): 
    return a + b


def logarithm(a,b):
    return math.log(a,b)


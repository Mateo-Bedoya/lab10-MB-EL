"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
#https://github.com/Mateo-Bedoya/lab10-MB-EL.git
#Mateo Bedoya
#Ezra Linnan
import math
def square_root(a):
    try:
        return math.sqrt(a)
    except a < 0:
        raise ValueError

def hypotenuse(a,b):
    return math.hypot(a,b)
# First example
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ZeroDivisionError("Cannot divide by zero")

def log(a, b):
    try:
        return math.log(a, b)
    except ValueError:
        raise ValueError("Cannot use log on negative numbers")

def exp(a, b):
    return a ** b

# First example
def add(a, b): 
    return a + b


def logarithm(a,b):
    return math.log(a,b)



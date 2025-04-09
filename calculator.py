"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

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
        print("Cannot divide by zero")

def log(a, b):
    try:
        return math.log(a, b)
    except ValueError:
        print("Cannot use log on negative numbers.")

def exp(a, b):
    return a ** b

# First example
def add(a, b): 
    return a + b

def multiply(a,b):
    return a *b

def divide(a,b):
    try:
        return b / a
    except a ==0:
        raise ZeroDivisionError

def logarithm(a,b):
    return math.log(a,b)

def exponent(a,b):
    return a ** b

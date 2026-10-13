"""
Instructions
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five()))    #  must return 35
four(plus(nine()))      #  must return 13
eight(minus(three()))   #  must return 5
six(divided_by(two()))  #  must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:
eight(divided_by(three()))

Given Code:
def zero(): pass #your code here
def one(): pass #your code here
def two(): pass #your code here
def three(): pass #your code here
def four(): pass #your code here
def five(): pass #your code here
def six(): pass #your code here
def seven(): pass #your code here
def eight(): pass #your code here
def nine(): pass #your code here

def plus(): pass #your code here
def minus(): pass #your code here
def times(): pass #your code here
def divided_by(): pass #your code here
"""

# Note: Didn't figure this out on my own. Ended up using ChatGPT to teach about about optional variables, passing functions as arguments, and used W3 Schools to learn about Lambda functions.
def zero(variable=None):
    if variable:
        return variable(0)
    return 0

def one(variable=None):
    if variable:
        return variable(1)
    return 1

def two(variable=None):
    if variable:
        return variable(2)
    return 2

def three(variable=None):
    if variable:
        return variable(3)
    return 3

def four(variable=None):
    if variable:
        return variable(4)
    return 4

def five(variable=None):
    if variable:
        return variable(5)
    return 5
def six(variable=None):
    if variable:
        return variable(6)
    return 6

def seven(variable=None):
    if variable:
        return variable(7)
    return 7

def eight(variable=None):
    if variable:
        return variable(8)
    return 8

def nine(variable=None):
    if variable:
        return variable(9)
    return 9

def plus(right):
    return lambda left: left + right

def minus(right):
    return lambda left: left - right

def times(right):
    return lambda left: left * right
def divided_by(right):
    return lambda left: left // right

# Tests
print(seven(times(five()))) # should be 35
print(four(plus(nine()))) # Should be 13
print(eight(minus(three()))) # Should be 5
print(six(divided_by(two()))) # Should be 3
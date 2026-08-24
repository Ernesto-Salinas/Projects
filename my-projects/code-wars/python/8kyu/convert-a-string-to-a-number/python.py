"""
Instructions:
Note: This kata is inspired by Convert a Number to a String!. Try that one too.

Description
We need a function that can transform a string into a number. What ways of achieving this do you know?

Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of an integral number.

Examples
"1234" --> 1234
"605"  --> 605
"1405" --> 1405
"-7" --> -7

Given Code:
def string_to_number(s):
    # your code here
    pass
"""

def string_to_number(s):
    return int(s)
    pass

# Tests
print(string_to_number("1234"))
print(string_to_number("605"))
print(string_to_number("1405"))
print(string_to_number("-7"))
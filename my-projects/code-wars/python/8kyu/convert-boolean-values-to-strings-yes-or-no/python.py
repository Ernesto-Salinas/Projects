"""
Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

Given Code:
def bool_to_word(boolean):
    # TODO
"""

def bool_to_word(boolean):
    if boolean is True:
        return "Yes"
    elif boolean is False:
        return "No"

# Tests
print(bool_to_word(True))
print(bool_to_word(False))
print(bool_to_word("Yes"))
    
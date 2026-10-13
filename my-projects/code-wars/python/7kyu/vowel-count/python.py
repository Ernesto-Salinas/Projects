"""
Instructions:
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.

Given Code:
def get_count(sentence):
    pass
"""

def get_count(sentence):
    count = 0
    for char in sentence.lower():
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            count+=1
    return count

# Tests

print(get_count("aeiou")) # Should be 5
print(get_count("y")) # Should be 0
print(get_count("bcdfghjklmnpqrstvwxz y")) # should be 0
print(get_count("")) # Should be 0
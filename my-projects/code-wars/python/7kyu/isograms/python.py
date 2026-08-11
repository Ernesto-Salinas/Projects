"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true
"aba" --> false
"moOse" --> false (ignore letter case)

Given Code:
def is_isogram(string):
    #your code here
"""

def is_isogram(string):
    string = string.lower()
    for i in string:
        count=0
        for x in string:
            if i == x:
                count+=1
            if count >=2:
                return False
    return True

# Tests
print(is_isogram("Dermatoglyphics"))
print(is_isogram("isogram"))
print(is_isogram("aba"))
print(is_isogram("moOse"))
print(is_isogram("isIsogram"))
print(is_isogram(""))
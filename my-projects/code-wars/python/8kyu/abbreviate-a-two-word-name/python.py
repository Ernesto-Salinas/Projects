"""
Instructions
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

patrick feeney => P.F

Given Code:
def abbrev_name(name):
    return
"""

def abbrev_name(name):
    first_last = name.split()
    return "".join(first_last[0][0].upper()+"."+first_last[1][0].upper())

# Tests
print(abbrev_name("Sam Harris"))
print(abbrev_name("patrick feenan"))
print(abbrev_name("Evan C"))
print(abbrev_name("P Favuzzi"))
print(abbrev_name("David Mendieta"))
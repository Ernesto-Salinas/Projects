"""
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]

Given Code:
def unique_in_order(sequence):
    return
"""

def unique_in_order(sequence):
    ans = []
    count = 0
    for char in sequence:
        if count == 0:
            ans.append(char)
            count+=1
            continue
        elif char == sequence[count-1]:
            count+=1
            continue
        else:
            ans.append(char)
            count+=1
    return ans

# Tests
print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order('ABBCcAD'))
print(unique_in_order([1, 2, 2, 3, 3]))
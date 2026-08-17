"""
Instructions:
Your task is to construct a building which will be a pile of n cubes. The cube at the bottom will have a volume of n*3, the cube above will have volume of (n-1)*3 and so on until the top which will have a volume of 1*3.

You are given the total volume m of the building. Being given m can you find the number n of cubes you will have to build?

The parameter of the function findNb (find_nb, find-nb, findNb, ...) will be an integer m and you have to return the integer n such as n*3 + (n-1)*3 + (n-2)*3 + ... + 1*3 = m if such a n exists or -1 if there is no such n.

Examples:
findNb(1071225) --> 45

findNb(91716553919377) --> -1

Given Code:
def find_nb(m):
    pass
"""

def find_nb(m):
    n = 1
    cubed_total = 0
    while cubed_total < m:
        cubed_total += n**3
        if cubed_total == m:
            return n
        n+=1
    return -1

# Tests
print(find_nb(9)) # Should be 2
print(find_nb(36)) # Should be 3
print(find_nb(100)) # Should be 4
print(find_nb(225)) # Should be 5
print(find_nb(1071225)) # Should be 45
print(find_nb(91716553919377)) # Should be -1
print(find_nb(4)) # Should be -1
print(find_nb(4183059834009)) # Should be 2022
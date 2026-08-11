"""
Instructions:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Additionally, if the number is negative, return 0.

Note: If a number is a multiple of both 3 and 5, only count it once.

Courtesy of projecteuler.net (Problem 1)

Given Code:
def solution(number):
    pass
"""


def solution(number):
    multiples=set()
    ans=0
    if number < 0:
        return 0
    for i in range(number):
        if i%3==0:
            multiples.add(i)
        if i%5==0:
            multiples.add(i)
    for x in multiples:
        ans+=x
    return ans
        

# Tests
print(solution(10)) # Should be 23 (3+5+6+9=23)
print(solution(4)) # Should be 3
print(solution(6)) # Should be 8 (3+5=8)
print(solution(16)) # Should be 60 (3+5+6+9+10+12+15=60)
print(solution(3)) # Should be 0
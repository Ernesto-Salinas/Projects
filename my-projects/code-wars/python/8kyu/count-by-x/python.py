"""
Description:
Create a function with two arguments that will return an array of the first n multiples of x.

Assume both the given number and the number of times to count will be positive numbers greater than 0.

Return the results as an array or list ( depending on language ).

Examples
x = 1, n = 10 --> [1,2,3,4,5,6,7,8,9,10]
x = 2, n = 5  --> [2,4,6,8,10]

Given Code:
def count_by(x, n):
    # Return a sequence of numbers counting by `x` `n` times.
    
"""

def count_by(x, n):
    y=x
    ans=[]
    for i in range(n):
        ans.append(y)
        y+=x
    return ans

# Tests
print(count_by(1, 5)) # Should be [1, 2, 3, 4, 5]
print(count_by(2, 5)) # Should be [2, 4, 6, 8, 10]
print(count_by(3, 5)) # Should be [3, 6, 9, 12, 15]
print(count_by(50, 5)) # Should be [50, 100, 150, 200, 250]
print(count_by(100, 5)) # Should be [100, 200, 300, 400, 500]

        
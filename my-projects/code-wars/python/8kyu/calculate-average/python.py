"""
Write a function which calculates the average of the numbers in a given array.

Note: Empty arrays should return 0.
"""

def find_average(numbers):
    sum=0
    n=0
    if numbers == []:
        return 0
    else:
        for x in numbers:
            sum+=x
            n+=1
        return sum/n

# Tests
print(find_average([1, 2, 3]))
print(find_average([12, 6, 4, 7]))
print(find_average([]))

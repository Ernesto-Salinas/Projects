"""
Description:
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

1 -->  1
2 --> 3 + 5 = 8

Given Code:
def row_sum_odd_numbers(n):
    #your code here
"""

def row_sum_odd_numbers(n):
    base = -1
    num = 1
    while (num-1) != n:
        arr = []
        for x in range(num):
            arr.append(base+2)
            base+=2
        num+=1
    print(sum(arr))

# Tests

"""
row_sum_odd_numbers(1)
row_sum_odd_numbers(2)
row_sum_odd_numbers(13)
row_sum_odd_numbers(19)
row_sum_odd_numbers(41)
"""

import pytest

def test_row_sum_odd_numbers():
    assert test_row_sum_odd_numbers(2) == 8
    assert test_row_sum_odd_numbers(3) == 27
    
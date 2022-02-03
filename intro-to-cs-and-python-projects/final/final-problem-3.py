# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 21:20:20 2021

@author: Desktop

Class Final - Problem 3

Implement a function that meets the specifications below.

def sum_digits(s):
    "" assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. ""
    # Your code here
For example, sum_digits("a;35d4") returns 12.

Paste your entire function, including the definition, in the box below. Do not leave any debugging print statements.
"""

def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    num="0123456789"
    ans=0
    for i in s:
        if i in num:
            ans+=int(i)
    if ans != 0:
        return ans
    else:
        raise ValueError


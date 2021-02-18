# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 00:43:50 2021

@author: Desktop
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b==0:
        return a
    else:
        return gcdRecur(b,a%b)
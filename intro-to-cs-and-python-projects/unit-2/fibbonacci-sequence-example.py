# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 22:25:01 2021

@author: Desktop
"""

def fib(n):
    '''
    a, b: positive integers
    
    returns: a positive integer, number of females alive in that month
    '''
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
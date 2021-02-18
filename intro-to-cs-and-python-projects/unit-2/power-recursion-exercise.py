# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 20:51:33 2021

@author: Desktop
"""

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    else:
        return base*recurPower(base, exp-1)
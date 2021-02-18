# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 20:18:00 2021

@author: Desktop
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    ans=1
    while exp>0:
        ans*=base
        exp-=1
    else:
        return ans
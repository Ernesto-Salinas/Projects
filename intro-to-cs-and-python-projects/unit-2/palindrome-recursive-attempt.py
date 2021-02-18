# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 23:36:17 2021

@author: Ernesto
"""

def pal(x):
    """ x is a string
    produces boolean saying if string is palindrome"""
    if len(x)==0 or len(x)==1:
        return True
    elif x[0]==x[(len(x))-1]:
        return pal(x[1:len(x)-1])
    else:
        return False
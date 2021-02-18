# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 00:25:18 2021

@author: Desktop
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr)==0:
        return False
    elif char==aStr[(len(aStr)-1)//2]:
        return True
    else:
        return isIn(char, (aStr.replace(aStr[(len(aStr)-1)//2],'')))
print(isIn("o", "johnson"))
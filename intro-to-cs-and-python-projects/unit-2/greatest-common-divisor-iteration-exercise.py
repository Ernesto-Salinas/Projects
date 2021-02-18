# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 00:14:08 2021

@author: Desktop
"""

def gcd(a,b):
    if a>=b:
        for x in reversed(range(0,b+1)):
            if b%x==0 and a%x==0:
                return x
                break
    else:
        for x in reversed(range(0,a+1)):
            if a%x==0 and b%x==0:
               return x
               break
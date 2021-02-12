# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 20:15:23 2021

@author: Desktop

Find the square root of x
"""

x=26
e=0.000001
num_g=1
hi_g=x+1
low_g=0
g=(hi_g+low_g)/2
while abs(g**2-x)>=e:
    num_g+=1
    if g**2>x:
        hi_g=g
        g=(g+low_g)/2
    elif g**2<x:
        low_g=g
        g=(g+hi_g)/2
print("The square root of 25 is approximately "+str(g))
print("It took", num_g, "guesses to get to this answer")
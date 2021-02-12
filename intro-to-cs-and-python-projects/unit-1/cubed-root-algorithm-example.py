# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 20:14:16 2021

@author: Desktop
"""

x= int(input('Enter an integer: '))
ans= 0
while ans**3 < x:
    ans = ans + 1
if ans**3 != x:
    print(str(x) + ' is not a perfect cube')
else:
    print('Cube root of '+ str(x) + ' is ' + str(ans))
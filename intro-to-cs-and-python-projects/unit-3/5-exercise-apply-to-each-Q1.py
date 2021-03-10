# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 21:14:33 2021

@author: Desktop

Exercise: apply to each 1

Here is the code for a function applyToEach:

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
Assume that  testList = [1, -4, 8, -9]

Desired result:
  >>> print(testList)
  [1, 4, 8, 9]
"""

testList = [1, -4, 8, -9]
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
def a(b):
    return abs(b)
applyToEach(testList,a)
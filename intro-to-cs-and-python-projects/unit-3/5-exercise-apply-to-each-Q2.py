# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 21:24:00 2021

@author: Desktop

Exercise: apply to each 1

Here is the code for a function applyToEach:

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
Assume that  testList = [1, -4, 8, -9]

Desired result:
>>> print(testList)
  [2, -3, 9, -8]
"""

testList = [1, -4, 8, -9]
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
def a(b):
    return b+1
applyToEach(testList,a)
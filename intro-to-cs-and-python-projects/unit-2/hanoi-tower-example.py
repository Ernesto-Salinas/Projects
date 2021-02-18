# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 22:56:09 2021

@author: Desktop
"""
def printMove(a,b):
    print("move from " + str(a) + " to " + str(b))

def towers(n,a,b,c):
    if n == 1:
        printMove(a,b)
    else:
        towers(n-1,a,c,b)
        towers(1,a,b,c)
        towers(n-1,c,b,a)

print(towers(3,"P1","P2","P3"))
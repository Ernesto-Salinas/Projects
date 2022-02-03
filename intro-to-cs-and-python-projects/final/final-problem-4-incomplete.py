# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 23:09:34 2021

@author: Desktop
"""

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    y=[L[0]]
    z=[L[0]]
    lentest=[]
    inc=[]
    dec=[]
    ans=0
    for x in range(len(L)-1):
        if L[x+1]>=L[x]:
            y.append(L[x+1])
        else:
            y=[L[x+1]]
        if len(y)>len(inc):
            inc=y
    for x in range(len(L)-1):
        if L[x+1]<=L[x]:
            z.append(L[x+1])
        else:
            z=[L[x+1]]
        if len(z)>len(dec):
            dec=z
    if len(inc)>len(dec):
        for i in inc:
            ans+=i
        return ans
    elif len(inc)==len(dec):
        for a in L:
            lentest.append(a)
            if inc in lentest:
                for i in inc:
                    ans+=i
                return ans
            elif dec in lentest:
                for j in dec:
                    ans+=j
                return ans
    else:
        for j in dec:
            ans+=j
        return ans
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 20:27:09 2021

@author: Desktop
"""

def fact(n):
    """
    Parameters
    ----------
    n : int or float
    fact will return answer to n!

    """
    ans=1
    for x in reversed(range(1,n+1)):
        ans*=x
    return(ans)
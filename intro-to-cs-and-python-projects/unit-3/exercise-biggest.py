# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 20:04:39 2021

@author: Ernesto

Consider the following sequence of expressions:

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
We want to write some simple procedures that work on dictionaries to return information.

This time, write a procedure, called biggest, which returns the key corresponding to the entry with the largest number of values associated with it. If there is more than one such entry, return any one of the matching keys.

Example usage:

>>> biggest(animals)
'd'
"""

animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['donkey', 'dog', 'dingo']}

def biggest(aDict):
    high=0
    big=''
    for k,v in aDict.items():
        count=0
        count=len(v)
        if count>=high:
            high=count
            big=k
    return big
        
        
print(biggest(animals))
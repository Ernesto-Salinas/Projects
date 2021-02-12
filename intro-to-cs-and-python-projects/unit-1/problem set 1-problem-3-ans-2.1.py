# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 23:12:09 2021

@author: Desktop

Problem Set 1 - Problem 3

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
"""

y=""
vx=""
alpha=""
a1=""
s="abcdefghijklmnopqrstuvwxyz"
for x in (s):
    vx=x
    if y<=vx:
        y=vx
        alpha=(alpha + x)
    else:
        y=vx
        alpha=x
    if len(alpha)>len(a1):
            a1=alpha
print("Longest substring in alphabetical order is: " + a1)
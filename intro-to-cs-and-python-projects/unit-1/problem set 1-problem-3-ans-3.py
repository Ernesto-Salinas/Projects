# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 23:09:33 2021

@author: Desktop

Problem Set 1 - Problem 3

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
"""


s="gwfqedeydbdalmufxvpygwiv"
y=s[0]
ans=""
for x in range(len(s)-1):
    if s[x+1]>=s[x]:
        y+=s[x+1]
    else:
        y=s[x+1]
    if len(y)>len(ans):
        ans=y
print("Longest substring in alphabetical order is: " + ans)
        
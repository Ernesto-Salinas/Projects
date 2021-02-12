# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 21:46:22 2021

@author: Desktop

Problem 1
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
"""
vc=0
s="sam ben bin oh you"
for x in s:
    if x=="a" or x=="e" or x=="i" or x=="o" or x=="u":
        vc+=1
print("Number of vowels: " + str(vc))                
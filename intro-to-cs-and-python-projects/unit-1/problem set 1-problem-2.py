# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 22:38:31 2021

@author: Desktop

Problem 2

Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
"""
count=0
a=False
b=False
c=False
s="oboobbobobbqbobbogobobob"
for x in s:
    if not a and not b and not c and x=="b":
        a=True
    elif a and not b and not c:
        if x=="o":
            b=True
        elif x=="b":
            a=True
        else:
            a=False
    elif a and b and not c:
        if x=="b":
            c=True
            count+=1
            b=False
            c=False
        else:
            a=False
            b=False
    elif x=="b":
        a=True
    else:
        a=False
        b=False
        c=False
print("Number of times bob occurs is: " + str(count))
        
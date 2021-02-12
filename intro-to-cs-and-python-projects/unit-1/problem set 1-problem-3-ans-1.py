# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 22:57:03 2021

@author: Desktop

Problem Set 1 - Problem 3

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
"""

y=0
vx=0
alpha=""
a1=""
a2=""
a3=""
a4=""
a5=""
a6=""
a7=""
a8=""
a9=""
a10=""
s="abcdefghijklmnopqrstuvwxyz"
for x in (s+"a"):
    if x=="a":
        vx=1
        if y<=vx:
            y=vx
            alpha=(alpha + x)
        else:
            y=vx
            if a1=="":
                a1=alpha
                alpha=x
            elif a2=="":
                a2=alpha
                alpha=x
            elif a3=="":
                a3=alpha
                alpha=x
            elif a4=="":
                a4=alpha
                alpha=x
            elif a5=="":
                a5=alpha
                alpha=x
            elif a6=="":
                a6=alpha
                alpha=x
            elif a7=="":
                a7=alpha
                alpha=x
            elif a8=="":
                a8=alpha
                alpha=x
            elif a9=="":
                a9=alpha
                alpha=x
            elif a10=="":
                a10=alpha
                alpha=x
    elif x=="b":
        vx=2
        if y<=vx:
            y=vx
            alpha=(alpha + x)
        else:
            y=vx
            if a1=="":
                a1=alpha
                alpha=x
            elif a2=="":
                a2=alpha
                alpha=x
            elif a3=="":
                a3=alpha
                alpha=x
            elif a4=="":
                a4=alpha
                alpha=x
            elif a5=="":
                a5=alpha
                alpha=x
            elif a6=="":
                a6=alpha
                alpha=x
            elif a7=="":
                a7=alpha
                alpha=x
            elif a8=="":
                a8=alpha
                alpha=x
            elif a9=="":
                a9=alpha
                alpha=x
            elif a10=="":
                a10=alpha
                alpha=x
    elif x=="c":
        vx=3
        if y<=vx:
            y=vx
            alpha=(alpha + x)
        else:
            y=vx
            if a1=="":
                a1=alpha
                alpha=x
            elif a2=="":
                a2=alpha
                alpha=x
            elif a3=="":
                a3=alpha
                alpha=x
            elif a4=="":
                a4=alpha
                alpha=x
            elif a5=="":
                a5=alpha
                alpha=x
            elif a6=="":
                a6=alpha
                alpha=x
            elif a7=="":
                a7=alpha
                alpha=x
            elif a8=="":
                a8=alpha
                alpha=x
            elif a9=="":
                a9=alpha
                alpha=x
            elif a10=="":
                a10=alpha
                alpha=x
    elif x=="d":
        vx=4
        if y<=vx:
            y=vx
            alpha=(alpha + x)
        else:
            y=vx
            if a1=="":
                a1=alpha
                alpha=x
            elif a2=="":
                a2=alpha
                alpha=x
            elif a3=="":
                a3=alpha
                alpha=x
            elif a4=="":
                a4=alpha
                alpha=x
            elif a5=="":
                a5=alpha
                alpha=x
            elif a6=="":
                a6=alpha
                alpha=x
            elif a7=="":
                a7=alpha
                alpha=x
            elif a8=="":
                a8=alpha
                alpha=x
            elif a9=="":
                a9=alpha
                alpha=x
            elif a10=="":
                a10=alpha
                alpha=x
    elif x=="e":
        vx=5
        if y<=vx:
            y=vx
            alpha=(alpha + x)
        else:
            y=vx
            if a1=="":
                a1=alpha
                alpha=x
            elif a2=="":
                a2=alpha
                alpha=x
            elif a3=="":
                a3=alpha
                alpha=x
            elif a4=="":
                a4=alpha
                alpha=x
            elif a5=="":
                a5=alpha
                alpha=x
            elif a6=="":
                a6=alpha
                alpha=x
            elif a7=="":
                a7=alpha
                alpha=x
            elif a8=="":
                a8=alpha
                alpha=x
            elif a9=="":
                a9=alpha
                alpha=x
            elif a10=="":
                a10=alpha
                alpha=x
    elif x=="f":
        vx=6
        if y<=vx:
            y=vx
            alpha=(alpha + x)
        else:
            y=vx
            if a1=="":
                a1=alpha
                alpha=x
            elif a2=="":
                a2=alpha
                alpha=x
            elif a3=="":
                a3=alpha
                alpha=x
            elif a4=="":
                a4=alpha
                alpha=x
            elif a5=="":
                a5=alpha
                alpha=x
            elif a6=="":
                a6=alpha
                alpha=x
            elif a7=="":
                a7=alpha
                alpha=x
            elif a8=="":
                a8=alpha
                alpha=x
            elif a9=="":
                a9=alpha
                alpha=x
            elif a10=="":
                a10=alpha
                alpha=x
    elif x=="g":
        vx=7
        if y<=vx:
            y=vx
            alpha=(alpha + x)
        else:
            y=vx
            if a1=="":
                a1=alpha
                alpha=x
            elif a2=="":
                a2=alpha
                alpha=x
            elif a3=="":
                a3=alpha
                alpha=x
            elif a4=="":
                a4=alpha
                alpha=x
            elif a5=="":
                a5=alpha
                alpha=x
            elif a6=="":
                a6=alpha
                alpha=x
            elif a7=="":
                a7=alpha
                alpha=x
            elif a8=="":
                a8=alpha
                alpha=x
            elif a9=="":
                a9=alpha
                alpha=x
            elif a10=="":
                a10=alpha
                alpha=x
    elif x=="h":
        vx=8
        if y<=vx:
            y=vx
            alpha=(alpha + x)
        else:
            y=vx
            if a1=="":
                a1=alpha
                alpha=x
            elif a2=="":
                a2=alpha
                alpha=x
            elif a3=="":
                a3=alpha
                alpha=x
            elif a4=="":
                a4=alpha
                alpha=x
            elif a5=="":
                a5=alpha
                alpha=x
            elif a6=="":
                a6=alpha
                alpha=x
            elif a7=="":
                a7=alpha
                alpha=x
            elif a8=="":
                a8=alpha
                alpha=x
            elif a9=="":
                a9=alpha
                alpha=x
            elif a10=="":
                a10=alpha
                alpha=x
    elif x=="i":
        vx=9
        if y<=vx:
            y=vx
            alpha=(alpha + x)
        else:
            y=vx
            if a1=="":
                a1=alpha
                alpha=x
            elif a2=="":
                a2=alpha
                alpha=x
            elif a3=="":
                a3=alpha
                alpha=x
            elif a4=="":
                a4=alpha
                alpha=x
            elif a5=="":
                a5=alpha
                alpha=x
            elif a6=="":
                a6=alpha
                alpha=x
            elif a7=="":
                a7=alpha
                alpha=x
            elif a8=="":
                a8=alpha
                alpha=x
            elif a9=="":
                a9=alpha
                alpha=x
            elif a10=="":
                a10=alpha
                alpha=x
    elif x=="j":
        vx=10
        if y<=vx:
            y=vx
            alpha=(alpha + x)
        else:
            y=vx
            if a1=="":
                a1=alpha
                alpha=x
            elif a2=="":
                a2=alpha
                alpha=x
            elif a3=="":
                a3=alpha
                alpha=x
            elif a4=="":
                a4=alpha
                alpha=x
            elif a5=="":
                a5=alpha
                alpha=x
            elif a6=="":
                a6=alpha
                alpha=x
            elif a7=="":
                a7=alpha
                alpha=x
            elif a8=="":
                a8=alpha
                alpha=x
            elif a9=="":
                a9=alpha
                alpha=x
            elif a10=="":
                a10=alpha
                alpha=x
    elif x=="k":
        vx=11
        if y<=vx:
            y=vx
            alpha=(alpha + x)
        else:
            y=vx
            if a1=="":
                a1=alpha
                alpha=x
            elif a2=="":
                a2=alpha
                alpha=x
            elif a3=="":
                a3=alpha
                alpha=x
            elif a4=="":
                a4=alpha
                alpha=x
            elif a5=="":
                a5=alpha
                alpha=x
            elif a6=="":
                a6=alpha
                alpha=x
            elif a7=="":
                a7=alpha
                alpha=x
            elif a8=="":
                a8=alpha
                alpha=x
            elif a9=="":
                a9=alpha
                alpha=x
            elif a10=="":
                a10=alpha
                alpha=x
    elif x=="l":
        vx=12
        if y<=vx:
            y=vx
            alpha=(alpha + x)
        else:
            y=vx
            if a1=="":
                a1=alpha
                alpha=x
            elif a2=="":
                a2=alpha
                alpha=x
            elif a3=="":
                a3=alpha
                alpha=x
            elif a4=="":
                a4=alpha
                alpha=x
            elif a5=="":
                a5=alpha
                alpha=x
            elif a6=="":
                a6=alpha
                alpha=x
            elif a7=="":
                a7=alpha
                alpha=x
            elif a8=="":
                a8=alpha
                alpha=x
            elif a9=="":
                a9=alpha
                alpha=x
            elif a10=="":
                a10=alpha
                alpha=x
    elif x=="m":
        vx=13
        if y<=vx:
            y=vx
            alpha=(alpha + x)
        else:
            y=vx
            if a1=="":
                a1=alpha
                alpha=x
            elif a2=="":
                a2=alpha
                alpha=x
            elif a3=="":
                a3=alpha
                alpha=x
            elif a4=="":
                a4=alpha
                alpha=x
            elif a5=="":
                a5=alpha
                alpha=x
            elif a6=="":
                a6=alpha
                alpha=x
            elif a7=="":
                a7=alpha
                alpha=x
            elif a8=="":
                a8=alpha
                alpha=x
            elif a9=="":
                a9=alpha
                alpha=x
            elif a10=="":
                a10=alpha
                alpha=x
    elif x=="n":
        vx=14
        if y<=vx:
            y=vx
            alpha=(alpha + x)
        else:
            y=vx
            if a1=="":
                a1=alpha
                alpha=x
            elif a2=="":
                a2=alpha
                alpha=x
            elif a3=="":
                a3=alpha
                alpha=x
            elif a4=="":
                a4=alpha
                alpha=x
            elif a5=="":
                a5=alpha
                alpha=x
            elif a6=="":
                a6=alpha
                alpha=x
            elif a7=="":
                a7=alpha
                alpha=x
            elif a8=="":
                a8=alpha
                alpha=x
            elif a9=="":
                a9=alpha
                alpha=x
            elif a10=="":
                a10=alpha
                alpha=x
    elif x=="o":
        vx=15
        if y<=vx:
            y=vx
            alpha=(alpha + x)
        else:
            y=vx
            if a1=="":
                a1=alpha
                alpha=x
            elif a2=="":
                a2=alpha
                alpha=x
            elif a3=="":
                a3=alpha
                alpha=x
            elif a4=="":
                a4=alpha
                alpha=x
            elif a5=="":
                a5=alpha
                alpha=x
            elif a6=="":
                a6=alpha
                alpha=x
            elif a7=="":
                a7=alpha
                alpha=x
            elif a8=="":
                a8=alpha
                alpha=x
            elif a9=="":
                a9=alpha
                alpha=x
            elif a10=="":
                a10=alpha
                alpha=x
    elif x=="p":
        vx=16
        if y<=vx:
            y=vx
            alpha=(alpha + x)
        else:
            y=vx
            if a1=="":
                a1=alpha
                alpha=x
            elif a2=="":
                a2=alpha
                alpha=x
            elif a3=="":
                a3=alpha
                alpha=x
            elif a4=="":
                a4=alpha
                alpha=x
            elif a5=="":
                a5=alpha
                alpha=x
            elif a6=="":
                a6=alpha
                alpha=x
            elif a7=="":
                a7=alpha
                alpha=x
            elif a8=="":
                a8=alpha
                alpha=x
            elif a9=="":
                a9=alpha
                alpha=x
            elif a10=="":
                a10=alpha
                alpha=x
    elif x=="q":
        vx=17
        if y<=vx:
            y=vx
            alpha=(alpha + x)
        else:
            y=vx
            if a1=="":
                a1=alpha
                alpha=x
            elif a2=="":
                a2=alpha
                alpha=x
            elif a3=="":
                a3=alpha
                alpha=x
            elif a4=="":
                a4=alpha
                alpha=x
            elif a5=="":
                a5=alpha
                alpha=x
            elif a6=="":
                a6=alpha
                alpha=x
            elif a7=="":
                a7=alpha
                alpha=x
            elif a8=="":
                a8=alpha
                alpha=x
            elif a9=="":
                a9=alpha
                alpha=x
            elif a10=="":
                a10=alpha
                alpha=x
    elif x=="r":
        vx=18
        if y<=vx:
            y=vx
            alpha=(alpha + x)
        else:
            y=vx
            if a1=="":
                a1=alpha
                alpha=x
            elif a2=="":
                a2=alpha
                alpha=x
            elif a3=="":
                a3=alpha
                alpha=x
            elif a4=="":
                a4=alpha
                alpha=x
            elif a5=="":
                a5=alpha
                alpha=x
            elif a6=="":
                a6=alpha
                alpha=x
            elif a7=="":
                a7=alpha
                alpha=x
            elif a8=="":
                a8=alpha
                alpha=x
            elif a9=="":
                a9=alpha
                alpha=x
            elif a10=="":
                a10=alpha
                alpha=x
    elif x=="s":
        vx=19
        if y<=vx:
            y=vx
            alpha=(alpha + x)
        else:
            y=vx
            if a1=="":
                a1=alpha
                alpha=x
            elif a2=="":
                a2=alpha
                alpha=x
            elif a3=="":
                a3=alpha
                alpha=x
            elif a4=="":
                a4=alpha
                alpha=x
            elif a5=="":
                a5=alpha
                alpha=x
            elif a6=="":
                a6=alpha
                alpha=x
            elif a7=="":
                a7=alpha
                alpha=x
            elif a8=="":
                a8=alpha
                alpha=x
            elif a9=="":
                a9=alpha
                alpha=x
            elif a10=="":
                a10=alpha
                alpha=x
    elif x=="t":
        vx=20
        if y<=vx:
            y=vx
            alpha=(alpha + x)
        else:
            y=vx
            if a1=="":
                a1=alpha
                alpha=x
            elif a2=="":
                a2=alpha
                alpha=x
            elif a3=="":
                a3=alpha
                alpha=x
            elif a4=="":
                a4=alpha
                alpha=x
            elif a5=="":
                a5=alpha
                alpha=x
            elif a6=="":
                a6=alpha
                alpha=x
            elif a7=="":
                a7=alpha
                alpha=x
            elif a8=="":
                a8=alpha
                alpha=x
            elif a9=="":
                a9=alpha
                alpha=x
            elif a10=="":
                a10=alpha
                alpha=x
    elif x=="u":
        vx=21
        if y<=vx:
            y=vx
            alpha=(alpha + x)
        else:
            y=vx
            if a1=="":
                a1=alpha
                alpha=x
            elif a2=="":
                a2=alpha
                alpha=x
            elif a3=="":
                a3=alpha
                alpha=x
            elif a4=="":
                a4=alpha
                alpha=x
            elif a5=="":
                a5=alpha
                alpha=x
            elif a6=="":
                a6=alpha
                alpha=x
            elif a7=="":
                a7=alpha
                alpha=x
            elif a8=="":
                a8=alpha
                alpha=x
            elif a9=="":
                a9=alpha
                alpha=x
            elif a10=="":
                a10=alpha
                alpha=x
    elif x=="v":
        vx=22
        if y<=vx:
            y=vx
            alpha=(alpha + x)
        else:
            y=vx
            if a1=="":
                a1=alpha
                alpha=x
            elif a2=="":
                a2=alpha
                alpha=x
            elif a3=="":
                a3=alpha
                alpha=x
            elif a4=="":
                a4=alpha
                alpha=x
            elif a5=="":
                a5=alpha
                alpha=x
            elif a6=="":
                a6=alpha
                alpha=x
            elif a7=="":
                a7=alpha
                alpha=x
            elif a8=="":
                a8=alpha
                alpha=x
            elif a9=="":
                a9=alpha
                alpha=x
            elif a10=="":
                a10=alpha
                alpha=x
    elif x=="w":
        vx=23
        if y<=vx:
            y=vx
            alpha=(alpha + x)
        else:
            y=vx
            if a1=="":
                a1=alpha
                alpha=x
            elif a2=="":
                a2=alpha
                alpha=x
            elif a3=="":
                a3=alpha
                alpha=x
            elif a4=="":
                a4=alpha
                alpha=x
            elif a5=="":
                a5=alpha
                alpha=x
            elif a6=="":
                a6=alpha
                alpha=x
            elif a7=="":
                a7=alpha
                alpha=x
            elif a8=="":
                a8=alpha
                alpha=x
            elif a9=="":
                a9=alpha
                alpha=x
            elif a10=="":
                a10=alpha
                alpha=x
    elif x=="x":
        vx=24
        if y<=vx:
            y=vx
            alpha=(alpha + x)
        else:
            y=vx
            if a1=="":
                a1=alpha
                alpha=x
            elif a2=="":
                a2=alpha
                alpha=x
            elif a3=="":
                a3=alpha
                alpha=x
            elif a4=="":
                a4=alpha
                alpha=x
            elif a5=="":
                a5=alpha
                alpha=x
            elif a6=="":
                a6=alpha
                alpha=x
            elif a7=="":
                a7=alpha
                alpha=x
            elif a8=="":
                a8=alpha
                alpha=x
            elif a9=="":
                a9=alpha
                alpha=x
            elif a10=="":
                a10=alpha
                alpha=x
    elif x=="y":
        vx=25
        if y<=vx:
            y=vx
            alpha=(alpha + x)
        else:
            y=vx
            if a1=="":
                a1=alpha
                alpha=x
            elif a2=="":
                a2=alpha
                alpha=x
            elif a3=="":
                a3=alpha
                alpha=x
            elif a4=="":
                a4=alpha
                alpha=x
            elif a5=="":
                a5=alpha
                alpha=x
            elif a6=="":
                a6=alpha
                alpha=x
            elif a7=="":
                a7=alpha
                alpha=x
            elif a8=="":
                a8=alpha
                alpha=x
            elif a9=="":
                a9=alpha
                alpha=x
            elif a10=="":
                a10=alpha
                alpha=x
    elif x=="z":
        vx=26
        if y<=vx:
            y=vx
            alpha=(alpha + x)
        else:
            y=vx
            if a1=="":
                a1=alpha
                alpha=x
            elif a2=="":
                a2=alpha
                alpha=x
            elif a3=="":
                a3=alpha
                alpha=x
            elif a4=="":
                a4=alpha
                alpha=x
            elif a5=="":
                a5=alpha
                alpha=x
            elif a6=="":
                a6=alpha
                alpha=x
            elif a7=="":
                a7=alpha
                alpha=x
            elif a8=="":
                a8=alpha
                alpha=x
            elif a9=="":
                a9=alpha
                alpha=x
            elif a10=="":
                a10=alpha
                alpha=x
if len(a1)>=len(a2) and len(a1)>=len(a3) and len(a1)>=len(a4) and len(a1)>=len(a5) and len(a1)>=len(a6) and len(a1)>=len(a7) and len(a1)>=len(a8) and len(a1)>=len(a9) and len(a1)>=len(a10):
    print("Longest substring in alphabetical order is: " + a1)
elif len(a2)>=len(a3) and len(a2)>=len(a4) and len(a2)>=len(a5) and len(a2)>=len(a6) and len(a2)>=len(a7) and len(a2)>=len(a8) and len(a2)>=len(a9) and len(a2)>=len(a10):
    print("Longest substring in alphabetical order is: " + a2)
elif len(a3)>=len(a4) and len(a3)>=len(a5) and len(a3)>=len(a6) and len(a3)>=len(a7) and len(a3)>=len(a8) and len(a3)>=len(a9) and len(a3)>=len(a10):
    print("Longest substring in alphabetical order is: " + a3)
elif len(a4)>=len(a5) and len(a4)>=len(a6) and len(a4)>=len(a7) and len(a4)>=len(a8) and len(a4)>=len(a9) and len(a4)>=len(a10):
    print("Longest substring in alphabetical order is: " + a4)
elif len(a5)>=len(a6) and len(a5)>=len(a7) and len(a5)>=len(a8) and len(a5)>=len(a9) and len(a5)>=len(a10):
    print("Longest substring in alphabetical order is: " + a5)
elif len(a6)>=len(a7) and len(a6)>=len(a8) and len(a6)>=len(a9) and len(a6)>=len(a10):
    print("Longest substring in alphabetical order is: " + a6)
elif len(a7)>=len(a8) and len(a7)>=len(a9) and len(a7)>=len(a10):
    print("Longest substring in alphabetical order is: " + a7)
elif len(a8)>=len(a9) and len(a8)>=len(a10):
    print("Longest substring in alphabetical order is: " + a8)
elif len(a9)>=len(a10):
    print("Longest substring in alphabetical order is: " + a9)
else:
    print("Longest substring in alphabetical order is: " + a10)
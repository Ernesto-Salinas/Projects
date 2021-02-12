# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 22:00:42 2021

@author: Desktop

In this problem, you'll create a program that guesses a secret number!

The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!
"""

print("Please think of a number between 0 and 100!")
high=100
low=0
y=""
while y!="c":
    g=(high+low)//2
    print("Is your secret number "+ str(g) + "?")
    y=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if y=="c":
        print("Game over. Your secret number was: " + str(g))
        break
    elif y=="h":
       high=g
    elif y=="l":
        low=g
    else:
        print("Sorry, I didn't understand your input.")
   
    

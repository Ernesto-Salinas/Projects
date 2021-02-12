# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 00:51:44 2021

@author: Desktop
"""

cube = 27
epsilon = 0.01
guess = 0.0
increment = 0.0001
num_guesses= 0
while abs(guess**3 -cube) >= epsilon:
    guess += increment
    num_guesses+= 1
print('num_guesses=', num_guesses)
if abs(guess**3 -cube) >= epsilon:
    print('Failed on cube root of', cube)
else:
    print(guess, 'is close to the cube root of', cube)




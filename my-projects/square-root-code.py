# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 20:15:23 2021

@author: Ernesto
(based off of or inspired by the code written by Eric Grimson of MIT)

Find the square root of x
"""
def square_root_1(x):
    e=0.000001
    num_g=1
    hi_g=x+1
    low_g=0
    g=(hi_g+low_g)/2
    while abs(g**2-x)>=e:
        num_g+=1
        if g**2>x:
            hi_g=g
            g=(g+low_g)/2
        elif g**2<x:
            low_g=g
            g=(g+hi_g)/2
    return "The square root of "+str(x)+" is approximately "+str(g)+"\nIt took "+str(num_g)+" guesses to get to this answer."

'''
8/26/2026 - New attempt
Find the square root of num

Basing function on formula: SqRt of num is approx the SqRt(Closest Square) + (difference of num & closest Square / 2 * SqRt(Closest Square))
'''

def square_root_2(num):
    closest_square = 0
    tolerance  = 0.000001
    for i in range(num):
        if i**2 <= num:
            closest_square = i
        else:
            break
    #print("the closest square is", closest_square)
    guess = closest_square+(abs(num-closest_square**2)/(2*closest_square))
    #print("initial guess is", guess)
    hi_guess = guess + 1
    low_guess = guess - 1
    num_of_guesses = 1
    while abs(guess**2-num)>=tolerance:
        num_of_guesses+=1
        if guess**2>num:
            hi_guess = guess
            guess = (low_guess+guess)/2
        elif guess**2<num:
            low_guess = guess
            guess = (hi_guess+guess)/2
    return "The square root of "+str(num)+" is approximately "+str(guess)+"\nIt took "+str(num_of_guesses)+" guesses to get to this answer."

print(square_root_1(1700001))


#Conclusion: While the new function (square_root_2) gets you a much more accurate initial guess,and a tighter high guess and low guess, it doesn't really help reduce the number of loops to arrive to an answer with a high accuracy, but you end up having to loop quite a bit to produce that initial guess if you're trying to find the square root of a higher number, so square_root_1 is better.
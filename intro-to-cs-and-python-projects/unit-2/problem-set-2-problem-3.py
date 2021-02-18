# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 19:25:30 2021

@author: Desktop
"""

n=12
balance=10000
annualInterestRate=0.20
ir=annualInterestRate/12
b1=balance
low=balance/12
high=(balance*((1+ir)**12))/12
p=(high+low)/2
while n>=0:
    ub=balance-p
    if n == 0:
        if balance>0:
            n=12
            balance=b1
            low=p
            p=(high+low)/2
        elif balance<-1:
            n=12
            balance=b1
            high=p
            p=(high+low)/2
        else:
            print("Lowest Payment:", round(p,2))
            break
    else:
        n-=1 
        balance=ub+((ir)*ub)
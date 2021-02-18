# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 19:25:30 2021

@author: Desktop
"""

n=12
balance=4773
b1=balance
annualInterestRate=0.2
p=10
while n>=0:
    ub=balance-p
    if n == 0:
        if balance>0:
            n=12
            balance=b1
            low=p
            p+=10
        elif balance<=0:
            print("Lowest Payment:", p)
            break
    else:
        n-=1 
        balance=ub+((annualInterestRate/12)*ub)
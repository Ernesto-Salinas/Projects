# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 18:29:10 2021

@author: Desktop
"""

n=12
balance=484
annualInterestRate=0.2
monthlyPaymentRate=0.04
while n>=0:
    p=balance*monthlyPaymentRate
    ub=balance-p
    if n == 0:
        print("Remaining balance:", round(balance, 2))
        break
    else:
        n-=1 
        balance=ub+((annualInterestRate/12)*ub)
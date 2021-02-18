# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 18:29:10 2021

@author: Desktop
"""

def rb(n,balance,annualInterestRate, monthlyPaymentRate):
    """
    Parameters
    ----------
    n : number of months
    balance : Outstanding balance on the credit card
    annualInterestRate : annual interest rate as a decimal
    monthlyPaymentRate : Minimum monthly payment rate as a decimal

    Returns
    -------
    remaining balance after making payments for "n" number of months
    """
    p=balance*monthlyPaymentRate
    ub=balance-p
    if n == 0:
        print("Remaining balance:", round(balance, 2))
    else:
        return rb(n-1, ub+((annualInterestRate/12)*ub), annualInterestRate, monthlyPaymentRate)
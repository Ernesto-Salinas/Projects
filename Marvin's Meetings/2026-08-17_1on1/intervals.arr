use context starter2024

# Forms of data definitions so far:
# - A single primitive datatype (e.g. Temperature as Number)
# - Enumeration (i.e. one of X things)

# NEW ONE: Intervals


# SITUATION: We are a tax software company, and we need to encode tax income brackets. 
# income <= 5000        ----> 0%
# 5000 < income <= 7500 ----> 5%
# 7500 < income <= 10000 ----> 10%
# otherwise             ----> 21%

# TASK: Given an income, we want to compute the tax percentage.

# square brackets is inclusive
# round parentheses is exclusive

# A TaxIncomeBracket is one of:
# - at most 5000
# - (5000, 7500]
# - (7500, 10000]
# - at least and excluding 10000
# INTERPRETATION: Represents a tax income bracket that a person would belong to.


#Examples
TIB_0 = 0
TIB_100 = 100
TIB_5000 = 5000
TIB_6000 = 6000
TIB_7500 = 7500
TIB_8000 = 8000
TIB_10000 = 10000
TIB_12000 = 12000

#Template
#Signature
#TaxIncomeBracket -> ?
fun tax-bracket-template(income):
  if income <= TIB_5000:
    ...
  else if (TIB_5000 < income) and (income <= TIB_7500):
    ...
  else if (TIB_7500 <= income) and (income < TIB_10000):
    ...
  else if income > TIB_10000:
    ...
  end
end



# Make more examples.
# Try to write the template. HINT: Similar to enumeration.
# I will send you the documentation on reactor.


#|


A TaxBracket is one of:
 - 0%
 - 5%
 - 10%
 - 21%
|#




# Signature
# Income -> TaxBracket

# Purpose Statement
# To figure out what tax bracket a person belongs to with a given income.
fun identify-tax-bracket(income):
  if income <= TIB_5000:
    0.00
  else if (TIB_5000 < income) and (income <= TIB_7500):
    0.05
  else if (TIB_7500 <= income) and (income < TIB_10000):
    0.10
  else if income > TIB_10000:
    0.21
  end
where:
  identify-tax-bracket(TIB_0) is 0.00
  identify-tax-bracket(TIB_6000) is 0.05
  identify-tax-bracket(TIB_8000) is 0.10
  identify-tax-bracket(TIB_12000) is 0.21
end

use context starter2024

# Forms of data definitions so far:
# - A single primitive datatype (e.g. Temperature as Number)
# - Enumeration (i.e. one of X things)

# NEW ONE: Intervals


# SITUATION: We are a tax software company, and we need to encode tax income brackets. 
# income <= 5000        ----> 0%
# 5000 < income <= 7500 ----> 5%
# 7500 < income < 10000 ----> 10%
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

TIB_0 = 0
TIB_100 = 100
TIB_5000 = 5000


# Make more examples.
# Try to write the template. HINT: Similar to enumeration.
# I will send you the documentation on reactor.

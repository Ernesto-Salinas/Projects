'''
Description:
Clock shows h hours, m minutes and s seconds after midnight.

Your task is to write a function which returns the time since midnight in milliseconds.

Example:
h = 0
m = 1
s = 1

result = 61000
Input constraints:

0 <= h <= 23
0 <= m <= 59
0 <= s <= 59

Given Code:
def past(h, m, s):
    # Good Luck!
'''

def past(h, m, s):
    ms = 0
    m += h*60
    s += m*60
    ms += s*1000
    return ms

#Tests

print(past(0,1,1)) #61000
print(past(1,1,1)) #3661000
print(past(0,0,0)) #0
print(past(1,0,1)) #3601000
print(past(1,0,0)) #3600000

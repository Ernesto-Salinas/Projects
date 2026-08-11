"""
Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

Note: a and b are not ordered!

Examples (a, b) --> output (explanation)
(1, 0) --> 1 (1 + 0 = 1)
(1, 2) --> 3 (1 + 2 = 3)
(0, 1) --> 1 (0 + 1 = 1)
(1, 1) --> 1 (1 since both are same)
(-1, 0) --> -1 (-1 + 0 = -1)
(-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)
Your function should only return a number, not the explanation about how you get that number.

Given Code:
def get_sum(a,b):
    #good luck!
"""

def get_sum(a,b):
    list1=[]
    if a==b:
        return a
    elif a < b:
        while a <= b:
            list1.append(a)
            a+=1
        return sum(list1)
    else:
        while b <= a:
            list1.append(b)
            b+=1
        return sum(list1)



# Tests
print(get_sum(0,1)) #Expect 1
print(get_sum(0,-1)) # Expect -1
print(get_sum(-1,2)) # Exect 2
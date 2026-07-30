"""
Description:
Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421
Input: 145263 Output: 654321
Input: 123456789 Output: 987654321

Given Code:
def descending_order(num):
    # Bust a move right here
"""


#Attempt 1"
def descending_order(num):
    PermHighInt="A"
    TempHighInt="0"
    num=str(num)
    while len(PermHighInt)-1 < len(num):
        for i in num:
            if i < PermHighInt[-1]:
                if i == TempHighInt[-1] and i != "0":
                    TempHighInt+=i
                if i > TempHighInt[-1]:
                    TempHighInt=i
        PermHighInt+=TempHighInt
        TempHighInt="0"
    PermHighInt = PermHighInt[1:]
    return (int(PermHighInt))

# Tests
print(descending_order(472))
print(descending_order(102))
print(descending_order(0))
print(descending_order(15))
print(descending_order(123456789))

#Attempt 2 after realizing there is a sorting method *facepalm*"

def descending_order_Att2(num):
    list1 = sorted(str(num))
    list1.reverse()
    ans=""
    for i in list1:
        ans+=i
    return(int(ans))

# Tests
print(descending_order_Att2(472))
print(descending_order_Att2(102))
print(descending_order_Att2(0))
print(descending_order_Att2(15))
print(descending_order_Att2(123456789))
"""
Description:
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !

Given Code:
def pig_it(text):
    #your code here
"""

def pig_it(text):
    ans=""
    for i in text.split():
        if i.isalnum():
            ans+=(i[1:]+i[0]+"ay ")
        else:
            ans+=(i+" ")
    return ans[:-1]

# Tests
print(pig_it('Pig latin is cool'))
print(pig_it('This is my string'))
print(pig_it('This is my string!'))
print(pig_it('Hello world !'))
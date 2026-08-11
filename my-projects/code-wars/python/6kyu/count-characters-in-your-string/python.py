"""
Instructions:
The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.

Given Code:
def count(s):
    # The function code should be here
    return {}
"""

def count(s):
    set1 = set()
    ans={}
    for i in s:
        set1.add(i)
    for i in set1:
        ans[i] = s.count(i)
    return ans

# Attempt 2 after reviewing other's answers. Dictionaries already remove duplicates so creating a set wasn't necessary.

def count2(s):
    ans={}
    for i in s:
        ans[i]=s.count(i)
    return ans


# Tests
print("Test attempt 1")
print(count('aba')) # Should be {'a': 2, 'b': 1}
print(count('')) # Should be {}
print(count('Hello!')) # Should be {'H': 1, 'e': 1, 'l': 2, 'o': 1}

print("Test attempt 2")
print(count2('aba')) # Should be {'a': 2, 'b': 1}
print(count2('')) # Should be {}
print(count2('Hello!')) # Should be {'H': 1, 'e': 1, 'l': 2, 'o': 1}
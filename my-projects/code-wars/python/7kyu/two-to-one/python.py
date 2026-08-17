"""
Instructions:
Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string (alphabetical ascending), the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

Given Code:
def longest(a1, a2):
    # your code
"""

def longest(a1, a2):
    ans = ""
    temp = set()
    for char in a1:
        temp.add(char)
    for char in a2:
        temp.add(char)
    list1 = list(temp)
    list1.sort()
    ans = ans.join(list1)
    return ans

# Tests
print(longest("aretheyhere", "yestheyarehere")) # Should be "aehrsty"
print(longest("loopingisfunbutdangerous", "lessdangerousthancoding")) # Should be "abcdefghilnoprstu"
print(longest("inmanylanguages", "theresapairoffunctions")) # Should be "acefghilmnoprstuy"
    
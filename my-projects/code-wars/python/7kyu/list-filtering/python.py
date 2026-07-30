"""
In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

Example
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

Given Code:
def filter_list(l):
    'return a new list with the strings filtered out'
"""

def filter_list(l):
    ans=[]
    for i in l:
        if not isinstance(i, str):
            ans.append(i)
        else:
            continue
    return(ans)

# Tests
print(filter_list([1, 2, 'a', 'b']))
print(filter_list([1,'a','b',0,15]))
print(filter_list([1,2,'aasf','1','123',123]))

"""
assert filter_list([1, 2, 'a', 'b']) == [1,2]
assert filter_list([1,'a','b',0,15]) == [1,0,15]
assert filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
"""
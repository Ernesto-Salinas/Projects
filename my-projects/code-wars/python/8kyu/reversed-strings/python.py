"""
Complete the solution so that it reverses the string passed into it.

'world'  =>  'dlrow'
'word'   =>  'drow'

Given Code:
def solution(string):
    pass
"""

def solution(string):
    return string[::-1]

#Tests
print(solution('world'))
print(solution('hello'))
print(solution(''))
print(solution('h'))
print(solution('string word one two three four'))

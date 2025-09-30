"""
Performing String Slicing Tasks

Write the Python code to perform the following string slicing tasks:
1. Print letter s from the string "Cats hate water"
2. Print integer 9 from the list [8,9,10]
3. Print the word "math" from the sentence "He doesn't teach math"
4. Print 1,2,3 from the statement "Testing 1, 2, 3"
5. Print A man, a plan, a canal from the sentence "A man, a plan, a canal: Panama"

Output:
s
9
math
1,2,3
A man, a plan, a canal
"""

catstr="Cats hate water"
print(catstr[3])

list8910=[8,9,10]
print(list8910[1])

mathstr="He doesn't teach math"
print(mathstr[-4:])

teststr="Testing 1, 2, 3"
print(teststr[-7:])

panstr="A man, a plan, a canal: Panama"
print(panstr[:22])
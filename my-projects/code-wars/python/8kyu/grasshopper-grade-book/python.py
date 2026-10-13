"""
Instructions:
Grade book
Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

Numerical Score	Letter Grade
90 <= score <= 100	'A'
80 <= score < 90	'B'
70 <= score < 80	'C'
60 <= score < 70	'D'
0 <= score < 60	'F'
Tested values are all between 0 and 100. Theres is no need to check for negative values or values greater than 100.

Given Code:
def get_grade(s1, s2, s3):
    # Code here
    return "F"
"""

def get_grade(s1, s2, s3):
    score = (s1+s2+s3)/3
    if 90 <= score:
        return "A"
    if 80 <= score and score < 90:
        return "B"
    if 70 <= score and score < 80:
        return "C"
    if 60 <= score and score < 70:
        return "D"
    if score < 60:
        return "F"

#Tests
print(get_grade(100, 85, 96)) #Should be "A"
print(get_grade(100, 100, 100)) #Should be "A"
print(get_grade(70, 70, 100)) #Should be "B"
print(get_grade(84, 79, 85)) #Should be "B"
print(get_grade(60, 82, 76)) #Should be "C"
print(get_grade(65, 70, 59)) #Should be "D"
print(get_grade(58, 59, 60)) #Should be "F"
print(get_grade(0, 0, 0)) #Should be "F"
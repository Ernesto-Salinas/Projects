"""
Instructions:
There was a test in your class and you passed it. Congratulations!

But you're an ambitious person. You want to know if you're better than the average student in your class.

You receive an array with your peers' test scores. Now calculate the average and compare your score!

Return true if you're better, else false!

Note:
Your points are not included in the array of your class's points. Do not forget them when calculating the average score!

Given Code:
def better_than_average(class_points, your_points):
    # Your code here
"""

def better_than_average(class_points, your_points):
    total = 0
    for score in class_points:
        total += score
    class_avg = total / len(class_points)
    return your_points > class_avg

# Tests
print(better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75)) # True
print(better_than_average([12, 23, 34, 45, 56, 67, 78, 89, 90], 69)) # False
print(better_than_average([41, 75, 72, 56, 80, 82, 81, 33], 50)) # True
days = int(input("Number of days? "))

"""
Using Arithmetic Operators
complete the Python code that takes user input as days and convers the days into years, weeks, days, and then prints them out.

Note: Ignore leap years.

Sample Input:
860

Sample Output:
Years: 2
Weeks: 18
Days: 4
"""
years = int(days/365)

days_remaining=days%365

weeks=int(days_remaining/7)

days=days_remaining%7

print("Years:", years)
print("Weeks:", weeks)
print("Days:", days)



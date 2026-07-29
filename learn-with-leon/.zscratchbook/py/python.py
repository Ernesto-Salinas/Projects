"""
def digitize(n):
    string1 = str(n)
    arr = []
    for num in n:
        print(num)
        arr = arr.append(num)
    print(arr)



digitize(4689)
"""

d = {1: "one", 2: "three"}
d1 = {2: "two"}
d.update(d1)
print (d)
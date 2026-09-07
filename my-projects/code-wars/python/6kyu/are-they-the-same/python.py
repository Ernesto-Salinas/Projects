"""
Instructions
Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whether the two arrays have the "same" elements, with the same multiplicities (the multiplicity of a member is the number of times it appears). "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

Examples
Valid arrays
a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a, b) returns true because in b 121 is the square of 11, 14641 is the square of 121, 20736 the square of 144, 361 the square of 19, 25921 the square of 161, and so on. It gets obvious if we write b's elements in terms of squares:

a = [121, 144, 19, 161, 19, 144, 19, 11] 
b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
Invalid arrays
If, for example, we change the first number to something else, comp is not returning true anymore:

a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a,b) returns false because in b 132 is not the square of any number of a.

a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
comp(a,b) returns false because in b 36100 is not the square of any number of a.

Remarks
a or b might be [] or {} (all languages except R, Shell).
a or b might be nil or null or None or nothing (except in C++, COBOL, Crystal, D, Dart, Elixir, Fortran, F#, Haskell, Nim, OCaml, Pascal, Perl, PowerShell, Prolog, PureScript, R, Racket, Rust, Shell, Swift).
If a or b are nil (or null or None, depending on the language), the problem doesn't make sense so return false.

Given Code:
def comp(array1, array2):
    # your code
"""


def comp(array1, array2):
    # This is in case the input is None
    if array1 == None or array2 == None:
        return False
    #Sort both arrays, square each element in array1, and if array1 and array 2 match, return True.
    #Because array1 can come in with negative values, array1 will be sorted after each element is squared.
    array2.sort()
    array1_sq = []
    for element in array1:
        array1_sq.append(element**2)
    array1_sq.sort()
    print("Array1 squared is ", array1_sq)
    print("Array2 is", array2)
    if array1_sq == array2:
        return True
    else:
        return False


# Tests

print(comp([121, 144, 19, 161, 19, 144, 19, 11], [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19])) # Should be True
print(comp([121, 144, 19, 161, 19, 144, 19, 11], [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19])) # Should be False
print(comp([-121, -144, 19, -161, 19, -144, 19, -11], [121, 14641, 20736, 361, 25921, 361, 20736, 361])) # Should be True
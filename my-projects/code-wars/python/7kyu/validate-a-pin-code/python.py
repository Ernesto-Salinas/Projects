"""
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.

Examples (Input --> Output)
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false

Given Code:
def validate_pin(pin):
    # return true or false
"""

def validate_pin(pin):
    if (len(pin) == 4 or len(pin) == 6) and pin.isdigit():
        return True
    else:
        return False


#Tests
print(validate_pin("1"))
print(validate_pin("12"))
print(validate_pin("123"))
print(validate_pin("1234")) #should be True
print(validate_pin("12345"))
print(validate_pin("123456")) #should be True
print(validate_pin("1234567"))
print(validate_pin("-1234"))
print(validate_pin("1.234"))
print(validate_pin("00000000"))
print(validate_pin("a234"))
'''
Instructions:
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

Given Code:
def is_pangram(st):
    return False
'''

def is_pangram(st):
    low_str = st.lower()
    abcs = "abcdefghijklmnopqrstuvwxyz"
    for letter in abcs:
        if letter in low_str:
            abcs = (abcs.replace(letter, ''))
    return (abcs == '')

# Tests
print(is_pangram("The quick brown fox jumps over the lazy dog.")) # Pangram
print(is_pangram("Cwm fjord bank glyphs vext quiz")) # Pangram
print(is_pangram("Pack my box with five dozen liquor jugs.")) # Pangram
print(is_pangram("How quickly daft jumping zebras vex.")) # Pangram
print(is_pangram("ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ")) # Pangram
print(is_pangram("This isn't a pangram!")) # Not pangram
print(is_pangram("abcdefghijklm opqrstuvwxyz")) # Not pangram
print(is_pangram("Aacdefghijklmnopqrstuvwxyz")) # Not pangram
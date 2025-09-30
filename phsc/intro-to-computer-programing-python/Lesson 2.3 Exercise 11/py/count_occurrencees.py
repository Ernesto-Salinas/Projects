"""
Activity 11: Manipulating Strings

Write a script that counts and displays the number of occurrences of a specified word in a given excertp. The script should request two input values from the user, that is, the excert and the word to search for. You can assume that the word will not occur as a substring in other words.

The steps are as follows:
1. Create a file named count_occurrences.py
2. Take in the suer input for the sentence and the query.
Next, sanitize and format the inupt by removing the whitespace and converting it to lowercase.
Count the occurences of the substring.
Print the results.
Run the script by using  the python count_occurrences.py command
"""

sentence=input()
query=input()

sentence = input("Sentence: ")
query = input("Word to look for in the sentence: ")

sentence=sentence.lower().strip()
query=query.lower().strip()
num=sentence.count(query)
print(f"There are {num} occurences of '{query}' in the sentence")
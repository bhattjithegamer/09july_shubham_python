import re

text = "Python is a powerful programming language."
word = "powerful"

# re.search() scans the entire string
match = re.search(word, text)

if match:
    print(f"Word '{word}' found in the string.")
else:
    print(f"Word '{word}' NOT found in the string.")

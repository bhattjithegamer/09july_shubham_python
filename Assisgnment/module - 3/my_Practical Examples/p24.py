import re

text = "Python is a powerful programming language."
word = "Python"

# re.match() checks only at the beginning of the string
match = re.match(word, text)

if match:
    print(f"Word '{word}' found at the beginning of the string.")
else:
    print(f"Word '{word}' NOT found at the beginning of the string.")

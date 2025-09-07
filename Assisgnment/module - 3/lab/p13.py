import re

# Input string and word
text = "Python is an easy language."
word = "Python"

# Match using re.match()
match = re.match(word, text)

if match:
    print(f"Word '{word}' found at the beginning of the string.")
else:
    print(f"Word '{word}' NOT found at the beginning of the string.")

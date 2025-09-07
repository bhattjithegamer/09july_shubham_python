import re

# Input string and word
text = "Python is a powerful programming language."
word = "powerful"

# Search using re.search()
match = re.search(word, text)

if match:
    print(f"Word '{word}' found at position {match.start()} to {match.end()}.")
else:
    print(f"Word '{word}' not found in the string.")

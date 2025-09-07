import re

sentence = "Python is fun and very powerful."
search_word = "powerful"

found = re.search(search_word, sentence)

if found:
    print(f"Word '{search_word}' found at position {found.start()} to {found.end()}.")
else:
    print(f"Word '{search_word}' not found in the string.")

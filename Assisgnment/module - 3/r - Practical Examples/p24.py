import re

sample_text = "Python is a powerful programming language."
search_word = "Python"

# re.match() checks only at the beginning of the string
match_result = re.match(search_word, sample_text)

if match_result:
    print(f"The word '{search_word}' was found at the beginning of the text.")
else:
    print(f"The word '{search_word}' was NOT found at the beginning of the text.")

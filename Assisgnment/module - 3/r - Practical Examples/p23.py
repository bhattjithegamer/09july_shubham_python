import re

sample_text = "Python is an amazing programming language."
search_word = "amazing"

# re.search() scans the entire string
found_match = re.search(search_word, sample_text)

if found_match:
    print(f"The word '{search_word}' was found in the text.")
else:
    print(f"The word '{search_word}' was NOT found in the text.")

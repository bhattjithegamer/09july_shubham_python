import re

sentence = "Python programming is fun."
search_word = "Python"

match_result = re.match(search_word, sentence)

if match_result:
    print(f"Word '{search_word}' found at the beginning of the string.")
else:
    print(f"Word '{search_word}' NOT found at the beginning of the string.")

multi_file = open("notes.txt", "w")

text_lines = [
    "Line one of the content\n",
    "Line two of the content\n",
    "Line three of the content\n"
]

multi_file.writelines(text_lines)

multi_file.close()

print("Multiple strings written to notes.txt successfully.")

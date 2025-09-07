# Using 'with' ensures the file is closed automatically
with open("myfile.txt", "w") as file:
    text = "Hello, this string will be written into the file."
    print(text, file=file)  # print() can directly write to a file

print("String has been written to myfile.txt")

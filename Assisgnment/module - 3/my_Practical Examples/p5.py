# Open the file in read mode
with open("myfile.txt", "r") as file:
    content = file.read()  # read entire file content
    print("Data from file:")
    print(content)

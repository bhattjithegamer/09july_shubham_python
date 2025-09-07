# Open the file in read mode
with open("custom_file.txt", "r") as my_file:
    file_content = my_file.read()  # read entire file content
    print("Data from the file:")
    print(file_content)

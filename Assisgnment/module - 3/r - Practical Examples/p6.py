with open("custom_file.txt", "r") as my_file:
    print("Initial cursor position:", my_file.tell())  # should be 0 at the start

    first_part = my_file.read(10)  # read first 10 characters
    print("Cursor position after reading 10 characters:", my_file.tell())

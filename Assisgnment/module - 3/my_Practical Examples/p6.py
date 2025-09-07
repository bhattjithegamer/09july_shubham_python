with open("myfile.txt", "r") as file:
    print("Initial cursor position:", file.tell())  # should be 0 at the start

    data = file.read(10)  # read first 10 characters
    print("Cursor position after reading 10 characters:", file.tell())

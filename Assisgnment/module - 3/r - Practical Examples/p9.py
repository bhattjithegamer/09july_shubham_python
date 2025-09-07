try:
    my_file = open("my_data.txt", "r")
    file_content = my_file.read()
    print("File content:")
    print(file_content)
except FileNotFoundError:
    print("Error: File does not exist.")
finally:
    # This will execute whether or not an exception occurred
    try:
        my_file.close()
        print("File closed successfully.")
    except NameError:
        print("File was never opened.")

try:
    file = open("data.txt", "r")
    content = file.read()
    print("File content:")
    print(content)
except FileNotFoundError:
    print("Error: File does not exist.")
finally:
    # This will execute whether or not an exception occurred
    try:
        file.close()
        print("File closed successfully.")
    except NameError:
        print("File was never opened.")

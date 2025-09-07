# Using 'with' ensures the file is closed automatically
with open("myfile.txt", "w") as my_file:
    message = "Hello Bhattji! This message is being saved into the file."
    print(message, file=my_file)  # print() can directly write to a file

print("Your custom message has been written to myfile.txt")

# Open a file in write mode (this will create the file if it doesn't exist)
my_file = open("example.txt", "w")

# String to write into the file
message = "Hello Bhattji! This is a custom message."

# Write the string to the file
my_file.write(message)

# Close the file
my_file.close()

print("Your message has been written to example.txt")

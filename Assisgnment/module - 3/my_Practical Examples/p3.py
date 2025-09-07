# Open a file in write mode (this will create the file if it doesn't exist)
file = open("example.txt", "w")

# String to write into the file
text = "Hello, this is a test string!"

# Write the string to the file
file.write(text)

# Close the file
file.close()

print("String has been written to example.txt")

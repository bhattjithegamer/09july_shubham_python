# Example string
txt = "shubham"

# Empty dictionary to store character counts
char_count = {}

# Counting characters using a for loop
for char in txt:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Printing the result
print("Character frequency:")
for key, value in char_count.items():
    print(f"{key}: {value}")

# String manipulation using methods
message = "   hello python world   "

print("Original String:", message)
print("Uppercase:", message.upper())          # Convert to uppercase
print("Lowercase:", message.lower())          # Convert to lowercase
print("Title Case:", message.title())         # Each word capitalized
print("Stripped:", message.strip())           # Remove leading/trailing spaces
print("Replace 'python' with 'Java':", message.replace("python", "Java"))
print("Check if starts with 'hello':", message.strip().startswith("hello"))
print("Check if ends with 'world':", message.strip().endswith("world"))
print("Split into words:", message.split())   # Split into list
print("Count 'o':", message.count('o'))       # Count occurrences of 'o')
print("Find 'python':", message.find("python"))  # Index of 'python'

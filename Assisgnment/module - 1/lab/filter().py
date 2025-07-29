# Filter out even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using filter with lambda
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print("Original List:", numbers)
print("Odd Numbers (even removed):", odd_numbers)

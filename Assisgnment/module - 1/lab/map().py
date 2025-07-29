# Square numbers using map()
numbers = [1, 2, 3, 4, 5]

# Using map with lambda
squared = list(map(lambda x: x ** 2, numbers))

print("Original List:", numbers)
print("Squared List:", squared)

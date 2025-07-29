from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Using reduce to calculate product
product = reduce(lambda x, y: x * y, numbers)

print("Numbers:", numbers)
print("Product of numbers:", product)

# List of fruits
list1 = ['apple', 'banana', 'mango']

print("Fruits except 'banana':")
for fruit in list1:
    if fruit == 'banana':
        continue  # Skip 'banana'
    print(fruit)

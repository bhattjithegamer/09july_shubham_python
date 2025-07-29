# List of fruits
list1 = ['apple', 'banana', 'mango']

print("Stop loop when 'banana' is found:")
for fruit in list1:
    if fruit == 'banana':
        print("Found 'banana', stopping loop.")
        break  # Stop the loop
    print(fruit)

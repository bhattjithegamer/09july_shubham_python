# List of fruits
list1 = ['apple', 'banana', 'mango']

# Take user input to search
search_fruit = input("Enter a fruit name to search: ")

found = False
for fruit in list1:
    if fruit == search_fruit.lower():  # case-insensitive match
        print(f"'{search_fruit}' is found in the list.")
        found = True
        break

if not found:
    print(f"'{search_fruit}' is NOT found in the list.")

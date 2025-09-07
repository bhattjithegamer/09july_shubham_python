try:
    file_name = input("Enter file name: ")
    my_file = open(file_name, "r")
    
    first_number = int(input("Enter a number: "))
    second_number = int(input("Enter another number: "))
    result = first_number / second_number
    print("Result:", result)

except FileNotFoundError:
    print("Error: File not found.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input, please enter numbers.")

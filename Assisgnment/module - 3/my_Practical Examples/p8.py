try:
    filename = input("Enter file name: ")
    file = open(filename, "r")
    
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:", result)

except FileNotFoundError:
    print("Error: File not found.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input, please enter numbers.")

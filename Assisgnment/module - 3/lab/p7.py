try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("Result:", result)

    # Accessing a list element
    my_list = [1, 2, 3]
    index = int(input("Enter an index to access (0-2): "))
    print("Value at index:", my_list[index])

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Invalid input! Please enter numbers only.")

except IndexError:
    print("Error: Index out of range!")

except Exception as e:
    print("Unexpected error:", e)

finally:
    print("Program execution completed.")

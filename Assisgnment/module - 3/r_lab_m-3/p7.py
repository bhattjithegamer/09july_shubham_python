try:
    first_value = int(input("Enter first number: "))
    second_value = int(input("Enter second number: "))
    division_result = first_value / second_value
    print("Result:", division_result)

    numbers = [10, 20, 30]
    position = int(input("Enter an index to access (0-2): "))
    print("Value at index:", numbers[position])

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Invalid input! Please enter numbers only.")

except IndexError:
    print("Error: Index out of range!")

except Exception as error:
    print("Unexpected error:", error)

finally:
    print("Program execution completed.")

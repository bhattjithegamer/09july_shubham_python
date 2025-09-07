def simple_calculator():
    try:
        # Take user input
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ")

        # Perform calculation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            # Check for division by zero
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero!")
            result = num1 / num2
        else:
            print("Invalid operation!")
            return

        print(f"Result: {result}")

    except ValueError:
        print("Invalid input! Please enter numeric values.")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the calculator
simple_calculator()

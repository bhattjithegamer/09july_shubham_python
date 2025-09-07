try:
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    operator = input("Enter operation (+, -, *, /): ")

    if operator == '+':
        result = first_number + second_number
    elif operator == '-':
        result = first_number - second_number
    elif operator == '*':
        result = first_number * second_number
    elif operator == '/':
        result = first_number / second_number
    else:
        raise ValueError("Invalid operation entered!")

    print("The result is:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError as ve:
    print("Error:", ve)
except Exception as e:
    print("Unexpected error:", e)

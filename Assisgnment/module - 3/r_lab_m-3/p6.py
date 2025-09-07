def basic_calculator():
    try:
        first_num = float(input("Enter first number: "))
        second_num = float(input("Enter second number: "))
        operator = input("Enter operation (+, -, *, /): ")

        if operator == '+':
            answer = first_num + second_num
        elif operator == '-':
            answer = first_num - second_num
        elif operator == '*':
            answer = first_num * second_num
        elif operator == '/':
            if second_num == 0:
                raise ZeroDivisionError("Cannot divide by zero!")
            answer = first_num / second_num
        else:
            print("Invalid operation!")
            return

        print(f"Result: {answer}")

    except ValueError:
        print("Invalid input! Please enter numeric values.")
    except ZeroDivisionError as err:
        print(f"Error: {err}")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")

basic_calculator()

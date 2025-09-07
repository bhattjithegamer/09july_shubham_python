class Calculator:
    # Method with default arguments
    def add_numbers(self, num1, num2=0, num3=0):
        return num1 + num2 + num3

# Create object
my_calculator = Calculator()

print("Sum of 2 numbers:", my_calculator.add_numbers(5, 10))       # uses 2 arguments
print("Sum of 3 numbers:", my_calculator.add_numbers(5, 10, 15))   # uses 3 arguments
print("Sum of 1 number:", my_calculator.add_numbers(5))            # uses 1 argument

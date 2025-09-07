# Define a custom exception
class NegativeNumberError(Exception):
    def __init__(self, number):
        super().__init__(f"Error: Negative number {number} is not allowed.")

try:
    num = int(input("Enter a positive number: "))
    if num < 0:
        raise NegativeNumberError(num)
    print("You entered:", num)
except NegativeNumberError as ne:
    print(ne)

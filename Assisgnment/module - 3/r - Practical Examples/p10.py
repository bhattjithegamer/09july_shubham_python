# Define a custom exception
class NegativeNumberError(Exception):
    def __init__(self, number):
        super().__init__(f"Error: Negative number {number} is not allowed.")

try:
    user_number = int(input("Enter a positive number: "))
    if user_number < 0:
        raise NegativeNumberError(user_number)
    print("You entered:", user_number)
except NegativeNumberError as ne:
    print(ne)

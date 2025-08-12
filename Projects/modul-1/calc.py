def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

while True:
    print("\nSimple Calculator")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Exiting Calculator... Bye!")
        break

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", sum(a, b))
    elif choice == '2':
        print("Result:", sub(a, b))
    elif choice == '3':
        print("Result:", mul(a, b))
    elif choice == '4':
        if b != 0:
            print("Result:", div(a, b))
        else:
            print("Error: Division by zero is not allowed!")
    else:
        print("Invalid choice! Please try again.")

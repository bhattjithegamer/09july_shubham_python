def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter choice: "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print(add(num1, num2))
elif choice == 2:
    print(sub(num1, num2))
elif choice == 3:
    print(mul(num1, num2))
elif choice == 4:
    print(div(num1, num2))
else:
    print("Invalid choice")

def add(m1, m2):
    return m1 + m2

def sub(m1, m2):
    return m1 - m2

def mul(m1, m2):
    return m1 * m2

def div(m1, m2):
    return m1 / m2

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter choice: "))
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

if choice == 1:
    print(add(x, y))
elif choice == 2:
    print(sub(x, y))
elif choice == 3:
    print(mul(x, y))
elif choice == 4:
    print(div(x, y))
else:
    print("Invalid choice")

class MathOperations:
    # Method with default arguments
    def add(self, a, b=0, c=0):
        return a + b + c

# Create object
math_op = MathOperations()

print("Add 2 numbers:", math_op.add(5, 10))      # uses 2 arguments
print("Add 3 numbers:", math_op.add(5, 10, 15)) # uses 3 arguments
print("Add 1 number:", math_op.add(5))          # uses 1 argument

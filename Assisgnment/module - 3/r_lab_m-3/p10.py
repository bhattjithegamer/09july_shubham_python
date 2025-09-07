# ---- Method Overloading (Simulated) ----
class MathOperations:
    # Simulating overloading using default parameters
    def add(self, x=None, y=None, z=None):
        if x is not None and y is not None and z is not None:
            return x + y + z
        elif x is not None and y is not None:
            return x + y
        else:
            return x

# ---- Method Overriding ----
class BaseClass:
    def show(self):
        print("This is BaseClass method.")

class DerivedClass(BaseClass):
    def show(self):  # Overriding BaseClass method
        print("This is DerivedClass method (Overridden).")


# ---- MAIN EXECUTION ----
print("=== Method Overloading Example ===")
math_op = MathOperations()
print("Add two numbers:", math_op.add(15, 25))
print("Add three numbers:", math_op.add(5, 10, 15))
print("Add one number:", math_op.add(50))

print("\n=== Method Overriding Example ===")
base_obj = BaseClass()
derived_obj = DerivedClass()
base_obj.show()
derived_obj.show()

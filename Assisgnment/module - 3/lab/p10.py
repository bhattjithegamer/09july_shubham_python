# ---- Method Overloading (Simulated) ----
class Calculator:
    # Simulating Overloading using default values
    def add(self, a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            return a + b + c
        elif a is not None and b is not None:
            return a + b
        else:
            return a

# ---- Method Overriding ----
class Parent:
    def display(self):
        print("This is Parent class method.")

class Child(Parent):
    def display(self):  # Overriding Parent's method
        print("This is Child class method (Overridden).")


# ---- MAIN EXECUTION ----
print("=== Method Overloading Example ===")
calc = Calculator()
print("Add two numbers:", calc.add(10, 20))        # Overloading simulation
print("Add three numbers:", calc.add(10, 20, 30))
print("Add one number:", calc.add(10))

print("\n=== Method Overriding Example ===")
parent_obj = Parent()
child_obj = Child()
parent_obj.display()   # Parent method
child_obj.display()    # Child overridden method

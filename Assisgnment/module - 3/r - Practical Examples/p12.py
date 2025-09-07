# Global variable
global_number = 100

# Define a class with a more descriptive name
class VariableDemo:
    def display_values(self):
        # Local variable
        local_number = 50
        print("Local variable value:", local_number)
        print("Global variable value:", global_number)

# Create an object of the class
demo_instance = VariableDemo()
demo_instance.display_values()

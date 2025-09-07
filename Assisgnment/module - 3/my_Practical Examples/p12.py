# Global variable
global_var = 100

class Demo:
    def show(self):
        # Local variable
        local_var = 50
        print("Local variable:", local_var)
        print("Global variable:", global_var)

# Create object
obj = Demo()
obj.show()

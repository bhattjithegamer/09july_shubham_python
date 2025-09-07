class Learner:
    # Constructor
    def __init__(self, full_name, years, subject):
        self.full_name = full_name
        self.years = years
        self.subject = subject

    # Method to display details
    def show_details(self):
        print(f"Name: {self.full_name}")
        print(f"Age: {self.years}")
        print(f"Subject: {self.subject}")


# Create an object of Learner class
learner1 = Learner("Bhatt Ji", 23, "Computer Science")

# Access properties using the object
print("Accessing Properties Directly:")
print("Name:", learner1.full_name)
print("Age:", learner1.years)
print("Subject:", learner1.subject)

# Access properties using a method
print("\nAccessing Properties using Method:")
learner1.show_details()

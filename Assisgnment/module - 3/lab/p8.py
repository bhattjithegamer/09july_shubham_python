class Student:
    # Constructor
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    # Method to display details
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")


# Create an object of Student class
student1 = Student("Bhatt Ji", 21, "BCA")

# Access properties using the object
print("Accessing Properties Directly:")
print("Name:", student1.name)
print("Age:", student1.age)
print("Course:", student1.course)

# Access properties using a method
print("\nAccessing Properties using Method:")
student1.display_info()

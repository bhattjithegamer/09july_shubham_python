# Define a class
class Person:
    def __init__(self, person_name, person_age):
        self.name = person_name  # property
        self.age = person_age    # property

# Create an object of the class
person1 = Person("User", 20)

# Access properties using the object
print("Name:", person1.name)
print("Age:", person1.age)

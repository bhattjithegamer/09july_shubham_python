# Define a class
class Person:
    def __init__(self, name, age):
        self.name = name  # property
        self.age = age    # property

# Create an object of the class
person1 = Person("Bhattji", 20)

# Access properties using the object
print("Name:", person1.name)
print("Age:", person1.age)

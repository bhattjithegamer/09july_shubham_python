# Parent class
class Animal:
    def sound(self):
        print("Animal makes a sound")

# Child class
class Dog(Animal):
    # Overriding the parent method
    def sound(self):
        print("Dog barks")

# Create objects
a = Animal()
d = Dog()

a.sound()  # calls parent method
d.sound()  # calls overridden method in child

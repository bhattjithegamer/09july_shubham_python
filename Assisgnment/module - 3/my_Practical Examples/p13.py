# Parent class
class Animal:
    def sound(self):
        print("Animal makes a sound")

# Child class inherits from Animal
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Object of child class
dog1 = Dog()
dog1.sound()  # inherited method
dog1.bark()   # own method

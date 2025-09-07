# Grandparent class
class Animal:
    def eat(self):
        print("Animal eats")

# Parent class
class Mammal(Animal):
    def walk(self):
        print("Mammal walks")

# Child class
class Dog(Mammal):
    def bark(self):
        print("Dog barks")

dog1 = Dog()
dog1.eat()   # from Animal
dog1.walk()  # from Mammal
dog1.bark()  # from Dog

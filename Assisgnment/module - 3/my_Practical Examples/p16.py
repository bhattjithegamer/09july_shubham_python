# Parent class
class Animal:
    def eat(self):
        print("Animal eats")

# Two child classes
class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

d = Dog()
c = Cat()

d.eat()
d.bark()
c.eat()
c.meow()

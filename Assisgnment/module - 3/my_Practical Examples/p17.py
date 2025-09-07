# Combination of multiple and multilevel inheritance

class Animal:
    def eat(self):
        print("Animal eats")

class Mammal(Animal):
    def walk(self):
        print("Mammal walks")

class Father:
    def skills(self):
        print("Father has programming skills")

class Child(Mammal, Father):
    def play(self):
        print("Child plays")

c = Child()
c.eat()    # from Animal
c.walk()   # from Mammal
c.skills() # from Father
c.play()   # own method

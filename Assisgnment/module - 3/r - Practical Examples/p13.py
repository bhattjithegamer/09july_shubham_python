# Parent class
class Creature:
    def make_noise(self):
        print("This creature makes a noise")

# Child class inherits from Creature
class Puppy(Creature):
    def bark_loudly(self):
        print("This puppy barks loudly")

# Object of child class
little_puppy = Puppy()
little_puppy.make_noise()    # inherited method
little_puppy.bark_loudly()   # own method

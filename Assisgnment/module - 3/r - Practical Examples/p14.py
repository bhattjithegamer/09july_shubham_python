# Grandparent class
class Creature:
    def consume_food(self):
        print("This creature eats food")

# Parent class
class MammalCreature(Creature):
    def take_walk(self):
        print("This mammal walks")

# Child class
class Puppy(MammalCreature):
    def make_bark_sound(self):
        print("This puppy barks")

# Object of the child class
my_puppy = Puppy()
my_puppy.consume_food()    # from Creature (grandparent)
my_puppy.take_walk()       # from MammalCreature (parent)
my_puppy.make_bark_sound() # from Puppy (child)

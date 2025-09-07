# Parent class
class Creature:
    def make_sound(self):
        print("This creature makes a sound")

# Child class
class Puppy(Creature):
    # Overriding the parent method
    def make_sound(self):
        print("This puppy barks loudly")

# Create objects
generic_creature = Creature()
my_puppy = Puppy()

generic_creature.make_sound()  # calls parent method
my_puppy.make_sound()          # calls overridden method in child

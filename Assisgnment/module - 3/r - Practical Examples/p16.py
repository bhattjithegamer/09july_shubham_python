# Parent class
class Creature:
    def consume_food(self):
        print("This creature eats food")

# Two child classes
class Puppy(Creature):
    def bark_loudly(self):
        print("This puppy barks loudly")

class Kitty(Creature):
    def meow_softly(self):
        print("This kitty meows softly")

# Create objects
my_puppy = Puppy()
my_kitty = Kitty()

# Call methods
my_puppy.consume_food()
my_puppy.bark_loudly()
my_kitty.consume_food()
my_kitty.meow_softly()

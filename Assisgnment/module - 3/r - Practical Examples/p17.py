# Grandparent class
class Creature:
    def consume_food(self):
        print("This creature eats food")

# Parent class (multilevel inheritance)
class MammalCreature(Creature):
    def take_walk(self):
        print("This mammal walks")

# Another parent class (multiple inheritance)
class ProgrammerParent:
    def programming_ability(self):
        print("This parent knows programming")

# Child class (combination of multilevel + multiple inheritance)
class TalentedChild(MammalCreature, ProgrammerParent):
    def play_game(self):
        print("This child plays games")

# Create object of the child class
super_kid = TalentedChild()
super_kid.consume_food()        # from Creature
super_kid.take_walk()           # from MammalCreature
super_kid.programming_ability() # from ProgrammerParent
super_kid.play_game()           # own method

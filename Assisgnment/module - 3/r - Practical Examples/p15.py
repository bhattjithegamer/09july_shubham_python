# First parent class
class ProgrammerParent:
    def programming_ability(self):
        print("This parent is skilled in programming")

# Second parent class
class ChefParent:
    def cooking_ability(self):
        print("This parent is skilled in cooking")

# Child inherits from both parents
class TalentedChild(ProgrammerParent, ChefParent):
    pass

super_kid = TalentedChild()
super_kid.programming_ability()  # from ProgrammerParent
super_kid.cooking_ability()      # from ChefParent

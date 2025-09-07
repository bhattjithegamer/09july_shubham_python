# First parent class
class Father:
    def skills(self):
        print("Father has programming skills")

# Second parent class
class Mother:
    def skills2(self):
        print("Mother has cooking skills")

# Child inherits from both
class Child(Father, Mother):
    pass

c = Child()
c.skills()
c.skills2()

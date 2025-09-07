# ---- Single Inheritance ----
class Base:
    def show_base(self):
        print("Single Inheritance: This is Base class.")

class Derived(Base):  # Single
    def show_derived(self):
        print("Single Inheritance: This is Derived class.")


# ---- Multiple Inheritance ----
class Dad:
    def show_dad(self):
        print("Multiple Inheritance: This is Dad class.")

class Mom:
    def show_mom(self):
        print("Multiple Inheritance: This is Mom class.")

class Kid(Dad, Mom):  # Multiple
    def show_kid(self):
        print("Multiple Inheritance: This is Kid class.")


# ---- Multilevel Inheritance ----
class Ancestor:
    def show_ancestor(self):
        print("Multilevel Inheritance: This is Ancestor class.")

class ParentLevel(Ancestor):
    def show_parent(self):
        print("Multilevel Inheritance: This is Parent class.")

class ChildLevel(ParentLevel):
    def show_child(self):
        print("Multilevel Inheritance: This is Child class.")


# ---- Hierarchical Inheritance ----
class CommonParent:
    def show_common_parent(self):
        print("Hierarchical Inheritance: This is Common Parent class.")

class FirstChild(CommonParent):
    def show_first_child(self):
        print("Hierarchical Inheritance: This is First Child class.")

class SecondChild(CommonParent):
    def show_second_child(self):
        print("Hierarchical Inheritance: This is Second Child class.")


# ---- Hybrid Inheritance ----
class Alpha:
    def show_alpha(self):
        print("Hybrid Inheritance: Class Alpha")

class Beta(Alpha):
    def show_beta(self):
        print("Hybrid Inheritance: Class Beta")

class Gamma(Alpha):
    def show_gamma(self):
        print("Hybrid Inheritance: Class Gamma")

class Delta(Beta, Gamma):  # Hybrid
    def show_delta(self):
        print("Hybrid Inheritance: Class Delta")


# ---- MAIN EXECUTION ----
print("\n--- Single Inheritance ---")
single = Derived()
single.show_base()
single.show_derived()

print("\n--- Multiple Inheritance ---")
multi = Kid()
multi.show_dad()
multi.show_mom()
multi.show_kid()

print("\n--- Multilevel Inheritance ---")
multi_level = ChildLevel()
multi_level.show_ancestor()
multi_level.show_parent()
multi_level.show_child()

print("\n--- Hierarchical Inheritance ---")
fchild = FirstChild()
schild = SecondChild()
fchild.show_common_parent()
fchild.show_first_child()
schild.show_common_parent()
schild.show_second_child()

print("\n--- Hybrid Inheritance ---")
hybrid = Delta()
hybrid.show_alpha()
hybrid.show_beta()
hybrid.show_gamma()
hybrid.show_delta()

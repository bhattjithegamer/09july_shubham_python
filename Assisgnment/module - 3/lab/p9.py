# ---- Single Inheritance ----
class Parent:
    def show_parent(self):
        print("Single Inheritance: This is Parent class.")

class Child(Parent):  # Single
    def show_child(self):
        print("Single Inheritance: This is Child class.")


# ---- Multiple Inheritance ----
class Father:
    def show_father(self):
        print("Multiple Inheritance: This is Father class.")

class Mother:
    def show_mother(self):
        print("Multiple Inheritance: This is Mother class.")

class ChildMultiple(Father, Mother):  # Multiple
    def show_child_multiple(self):
        print("Multiple Inheritance: This is Child class.")


# ---- Multilevel Inheritance ----
class GrandParent:
    def show_grandparent(self):
        print("Multilevel Inheritance: This is GrandParent class.")

class ParentLevel(GrandParent):
    def show_parent_level(self):
        print("Multilevel Inheritance: This is Parent class.")

class ChildLevel(ParentLevel):
    def show_child_level(self):
        print("Multilevel Inheritance: This is Child class.")


# ---- Hierarchical Inheritance ----
class ParentCommon:
    def show_parent_common(self):
        print("Hierarchical Inheritance: This is Common Parent class.")

class ChildOne(ParentCommon):
    def show_child_one(self):
        print("Hierarchical Inheritance: This is Child One class.")

class ChildTwo(ParentCommon):
    def show_child_two(self):
        print("Hierarchical Inheritance: This is Child Two class.")


# ---- Hybrid Inheritance ----
class A:
    def show_A(self):
        print("Hybrid Inheritance: Class A")

class B(A):
    def show_B(self):
        print("Hybrid Inheritance: Class B")

class C(A):
    def show_C(self):
        print("Hybrid Inheritance: Class C")

class D(B, C):  # Hybrid
    def show_D(self):
        print("Hybrid Inheritance: Class D")


# ---- MAIN EXECUTION ----
print("\n--- Single Inheritance ---")
single = Child()
single.show_parent()
single.show_child()

print("\n--- Multiple Inheritance ---")
multi = ChildMultiple()
multi.show_father()
multi.show_mother()
multi.show_child_multiple()

print("\n--- Multilevel Inheritance ---")
multi_level = ChildLevel()
multi_level.show_grandparent()
multi_level.show_parent_level()
multi_level.show_child_level()

print("\n--- Hierarchical Inheritance ---")
c1 = ChildOne()
c2 = ChildTwo()
c1.show_parent_common()
c1.show_child_one()
c2.show_parent_common()
c2.show_child_two()

print("\n--- Hybrid Inheritance ---")
hybrid = D()
hybrid.show_A()
hybrid.show_B()
hybrid.show_C()
hybrid.show_D()

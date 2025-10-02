class student:
    def display(self,id):
        print("id is",id)

class teacher(student):
    def display(self,name):
        return name      
te = teacher()
print(te.display(101))
print(te.display("shubham"))
class student:
    __age = 10

    def get(self):
       print("age is",self.__age)

    
class teacher(student):
    def show(self):
        print("age is",self.__age)
        

t = teacher()
t.show()
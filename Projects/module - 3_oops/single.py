class parent:
    id = 101
    name = "shubham"
    
        
class child(parent):
    age = 22
    city = "valasan"
    def show(self):
        print(self.id)
        print(self.name)
        print(self.age)
        print(self.city)

ch = child()
ch.show()

class parent:
    id = 101

class child(parent):
    name = "shubham"
    

class grandchild(child):
    age = 22
    city = "valasan"        

class shubham(grandchild):
    def final(self):
        print("id is ",self.id)
        print("name is ",self.name)
        print("age is ",self.age)
        print("city is ",self.city)


sh = shubham()
sh.final()

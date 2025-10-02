class a:
    id:int
    def getdata(self):
        self.id = input("Enter id: ")
class b:
    name:str
    def getdata1(self):
        self.name = input("Enter name: ")
class c:
    age:int
    def getdata2(self):
        self.age = input("Enter age: ")
class d(a,b,c):
    city:str
    def getdata3(self):
        self.city = input("Enter city: ")
        print("is is ",self.id)
        print("name is ",self.name)
        print("age is ",self.age)
        print("city is ",self.city)

d = d()
d.getdata()
d.getdata1()
d.getdata2()    
d.getdata3()
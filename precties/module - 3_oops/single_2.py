class parent:
    id:int
    name:str
    def getdata(self):
        self.id = input("Enter id: ")
        self.name = input("Enter name: ")
class child(parent):
    def show(self):
        print(self.id)
        print(self.name)
ch = child()
ch.getdata()
ch.show()
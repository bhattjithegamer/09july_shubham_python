class student:
    std_id:int
    name:str

    def display(self):
        self.input_id = int(input("enter id: "))
        self.input_name = input("enter name: ")

    def show(self):
        print("id",self.input_id)
        print("name",self.input_name)
st = student()
st.display()   
st.show()
std = {}
a = int(input("how many dict : "))
for i in range(a):
    key = input(f"enter key for dict {i + 1}: ")
    id = input("enter id : ")
    name = input("enter name : ")
    city = input("enter city : ")
    std[key] = {"id":id,"name":name,"city":city}

print(std)


    
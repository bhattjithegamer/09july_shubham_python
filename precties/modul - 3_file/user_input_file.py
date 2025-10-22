#user input mate program
y = open("bhattji.txt","a")

z = int(input("Enter number of students: "))
for i in range(z):
    a = input("Enter your name: ")
    b = input("Enter your age: ")
    y.write(f"\nName: {a} \nAge: {b}\n")


#=====creating a function======#
# def hello():
#     print("hello world")
# hello()

#=====function arbit======#
# def getdata (*data):
#     print("age is :",data[0])
#     print("name is :",data[1])
#     print("city is :",data[2])
# getdata(21,"bhatt ji","valasana")

#=====function default arg======#
# def getdata (name,age=22):
#     print("name is :",name)
#     print("age is :",age)
# getdata("bhatt ji")

##===function dict arg======#
# def getdata(data):
#     print("name is :",data["name"])
#     print("age is :",data["age"])
#     print("city is :",data["city"])
# getdata({"name":"bhatt ji","age":21,"city":"valasana"})

#=====function keyword======#
# def data(name,age,city):
#     print("name : ",name)
#     print("age : ",age)
#     print("city : ",city)
# data(age = 21 , city = "valasan" , name = "bhatt ji")

#=====function list arg======#
# def getdata(data):
#     print("name : ",data[0])
#     print("age : ",data[1])
#     print("city : ",data[2])
# getdata(["bhatt ji",21,"valasan"])

#=====function return======#
# def sum(a,b):
#     return a+b
# a = sum(10,20)
# print('ans is',a)

#=====function udf1======#
# def sum(a,b):
#     print("sum is : ",a+b)
# x = int(input("enter 1st num : "))
# y = int(input("enter 2nd num : "))
# sum(x,y)

#=====function udf2======#
# def data(name,age):
#     print("name : ",name)
#     print("age : ",age)
# data("bhatt ji",21)

#=====function udf3======#
# def data(name,age,city):
#     print("name : ",name)
#     print("age : ",age)
#     print("city : ",city)

# n = int(input("how many times you want to print : "))
# list = []

# for i in range(n):
#     a = input("enter name : ")
#     b = int(input("enter age : "))
#     c = input("enter city : ")
#     list.append((a,b,c))

# for i in list:
#     data(i[0],i[1],i[2])

#======task=======#
import sys
def sum (a,b):
    print("sum is : ",a+b)
def sub (a,b):
    print("sub is : ",a-b)
def mul (a,b):
    print("mul is : ",a*b)
def div (a,b):
    print("div is : ",a/b)

while True:
    print("1. sum\n2. sub\n3. mul\n4. div\n===exit===")

    choice = int(input("enter your choice : "))

    if choice == 5:
        exit("successfully exited")
        sys.exit()

    a = int(input("enter 1st num : "))
    b = int(input("enter 2nd num : "))

    if choice == 1:
        sum(a,b)
    elif choice == 2:
        sub(a,b)
    elif choice == 3:
        mul(a,b)
    elif choice == 4:
        div(a,b)
    else: 
        print("invalid choice")

    input("press enter to continue...")
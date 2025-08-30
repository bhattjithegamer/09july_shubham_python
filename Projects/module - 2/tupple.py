a = ('apple', 'banana', 'cherry', 'orange', 'kiwi')

#print(a[0]) #first element print karva mate
#print(a[-1]) #last element print karva mate
#print(a[0:3]) #ketla elements print karva che te mate
#print(a[1:]) #1 index thi last sudhi print karva mate
#print(a[:2]) #0 index thi 2 index sudhi print karva mate
#print(len(a)) #tupple ni length print karva mate

# if 'banana' in a:
#     print("yes")
# else:
#     print("no")

# for i in a:
#     print(i) #tupple ma che tevu line ma print karva mate

#print(a.index('cherry')) #index print karva mate

# del a
# print(a) #tupple delete karva mate

#a[1] = "kiwi" #tupple ma element change karva mate
#print(a) #error aavse tupple ma element change nai kari sakay karan ke tupple immutable che

#======================= #

name = ()

a = int(input("enter number: "))
for i in range(a):
    b = input("enter name : ")
    name = name + (b,)
print(name)  
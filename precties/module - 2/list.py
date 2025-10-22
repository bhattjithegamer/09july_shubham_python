#a = ["apple", "banana", "mango", "orange", "grapes"]

# ------------------------------------ #
#print(a[0]) #first element print karva mate
#print(a[-1]) #last element print karva mate
#print(a[2:4]) #ketla elements print karva che te mate
#print(a[1:]) #1 index thi last sudhi print karva mate
#print(a[:2]) #0 index thi 2 index sudhi print karva mate
#print(len(a)) #list ni length print karva mate

#for i in a:
#    print(i) #list ma che tevu line ma print karva mate

#print(a.index('mango')) #index print karva mate

# ========================= # 


#a[3]="c" #list ma element change karva mate

# if 'mango' in a:
#     print("yes")
# else:
#     print("no") #element che ke nai te check karva mate

# ========================== #

#a.append("kiwi") #list ma element add karva mate
#a.insert(1,"kiwi") #list ma koi pan index par element add karva mate
#a.remove("banana") #list ma thi element remove karva mate
#a.pop() #last element remove karva mate
#a.pop(1) #koi pan index parthi element remove karva mate
#a.clear() #list ma thi badha element remove karva mate
#a.sort() #list ne ascending order ma sort karva mate
#a.reverse() #list ne descending order ma sort karva mate
#del a #list delete karva mate
#del a[2] #koi pan index parthi element delete karva mate
#b = a.copy() #list ne copy karva mate
#print(b)
#a.extend(["kiwi","pineapple"]) #list ma ek thi vadhu element add karva mate
#print(a)


#===========dynamic list============== #


a = []

b = int(input("enter number: "))

for i in range(b):
    c = input("enter number: ")
    a.append(c)
print(a)





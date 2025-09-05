import keyword

x = keyword.kwlist
print(x)
print(len(x))

key=input("enter any keyword : ")

if key in x:
    print("this is keyword : ")
else:
    print("no it is not keyword : ")


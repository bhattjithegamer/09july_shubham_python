a = int(input ("Enter marks: "))
b = int(input ("Enter marks: "))
c = int(input ("Enter marks: "))
d = int(input ("Enter marks: "))

if a>= 40 and b >= 40 and c >= 40 and d >= 40:
    total = a + b + c + d
print("Total marks are: ", total)

avg = total / 4
print("Average marks are: ", avg)

if avg >= 80:
    print("You got grade A")

elif avg >= 60:
    print("You got grade B")

elif avg >=40 :
    print("you got grade C")

elif avg >= 30:
    print("you got grade D")
else: 
    print("u r fail")



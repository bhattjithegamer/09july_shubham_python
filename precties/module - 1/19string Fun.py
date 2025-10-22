# String Functions in Python
# a = "shubham bhatt"


# b = a.capitalize() #pelo words ke first letter ko capital karta hai
# b = a.casefold() # ye lower case karta hai
#b = a.center(50) # ye string ko center me le aata hai
#b = a.count("h") # ye count karta hai ki kitni baar h aaya hai
#b = a.endswith("h") # ye check karta hai ki string kis letter pe end ho rahi hai
#b = a.find("t") # ye find karta hai ki letter kaha pe hai
#b = a.format("") # ye string me format karta hai
#b = a.index("t") # ye find karta hai ki letter kaha pe hai
#b = a.isalnum() # ye check karta hai ki string me sirf alphabet aur number hai
#b = a.isidentifier() # ye check karta hai ki string valid identifier hai ya nahi
#b = a.islower() # ye check karta hai ki string lower case me hai ya nahi
#b = a.istitle() # ye check karta hai ki string title ka pehla word ka letter capital hai ya nahi
#b= a.isupper() # ye check karta hai ki string upper case me hai ya nahi
#b = a.join("''") # ye string ko join karta hai
#b = a.ijust() # ye string ko adjust karta hai, lekin isme koi change nahi aata
#b = a.partition("b") # ye string ko partition karta hai, yani ki string ko do part me baant deta hai
#b = a.replace("h", "H") # ye string me h ko H se replace karta hai
#b = a.split(" ") # ye string ko split karta hai, yani ki space ke hisab se alag alag words me baant deta hai
#b = a.swapcase() # ye string me upper case ko lower case aur lower case ko upper case me badal deta hai
#b = a.title() # ye string me har word ke pehle letter ko capital karta hai
# print(b)


#string Slicing in Python

a = "shubham bhatt"
# print(a[0]) # ye string me se 0 index ka letter print karega
#print(a[-1]) # ye string me se last index ka letter print karega
#print(a[0:4]) # ye string me se 0 se 4 index tak ke letters ko print karega
#print(a[2:]) # ye string me se 2 index se lekar end tak ke letters ko print karega
#print(a[:4]) # ye string me se start se lekar 4 index tak ke letters ko print karega
print(len(a))

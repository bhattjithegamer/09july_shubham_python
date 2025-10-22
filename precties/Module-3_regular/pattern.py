import re
email = input("Enter your email: ")
e = re.findall('[a-z]+[0-9]+@+[a-z]+.+[a-z]', email)
print(e)
if e:
    print("valid email")
else:
    print("invalid email")
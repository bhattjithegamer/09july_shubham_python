# USERNAME
a = input("Enter username: ")
if a.isalpha():
    print(" Valid username")
else:
    print(" Username should contain only letters")

# PASSWORD
b = input("Enter password: ")
if len(b) >= 6 and b.isalnum():
    print(" Valid password")
else:
    print(" Password must be at least 6 characters and alphanumeric")

# PHONE NUMBER
c = input("Enter phone number: ")
if c.isdigit() and len(c) == 10:
    print(" Valid phone number")
else:
    print(" Phone number must be 10 digits")

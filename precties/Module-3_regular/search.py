import re

a = "my self bhatt ji"
b = re.search("self",a)
print(b)

if b:
    print("yes")
else:
    print("no")
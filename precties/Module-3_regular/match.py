import re

a = "my self bhatt ji"
b = re.findall("ji", a)
print(b)
if b:
    print("yes")
else:
    print("no")
import re
a = "heloo 12546 kese ho"
# b = re.findall("12",a)
b = re.findall("[A-Z]",a)
print(b)
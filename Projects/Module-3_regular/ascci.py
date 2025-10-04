import re
a = "hello My self b352hatt ji"
# b = re.findall("\w",a) #aama bdha character aave
# b = re.findall("\W",a) #aama badha special character aave
# b = re.findall("\s",a) #aama badha space aave
# b = re.findall("\S",a) #aama badha space ne badha character aave
# b = re.findall("\d",a) #aama badha number aave
# b = re.findall("\D",a) #aama badha number ne badha character aave
# b = re.findall(r"\bhello",a) #aama badha word ni sharuvaat ma hello aave
b = re.findall("ji\Z",a) #aama badha word ni end ma 352 aave
print(b)
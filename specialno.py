import re
e=input()
s = re.findall("\W", e)
r=re.findall("_",e)
print(len(s)+len(r))



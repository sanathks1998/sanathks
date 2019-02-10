import re

e=input()
s = re.findall("\W", e)
print(len(s))



n=input()
r='0123456789'
count=0
for wl in n:
    for ls in r:
        if wl is ls: 
            count+=1
print(count)

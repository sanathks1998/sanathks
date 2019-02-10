r,c=input().split()
r,c=[int(r),int(c)]
r=r^c
c=r^c
r=r^c
print(r," ",c)

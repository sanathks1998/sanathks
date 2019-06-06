o=input()
l=list(o)
w=0
c=0
n=len(l)//2
l.remove(l[n])
r1=l[:n]
r2=l[n:]
r2.reverse()

if(r1==r2):
    print("YES")
else:
    print("NO")


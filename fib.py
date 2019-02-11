n=int(input())
f=0
l=1
i=0
t=0
for i in range(n):
    
    f=l
    l=t
    t=f+l
    print(t)

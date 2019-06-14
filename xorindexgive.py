r,s=map(int,input().split())
l=list(map(int,input().split()))
r=[]

l.insert(0,0)
for x in range(s):
     q=[]
     sums=0
     c,d=map(int,input().split())
     for i in range(c,d+1):
         
         sums^=l[i]
     
     r.append(sums)
for x in r:
    print(x)

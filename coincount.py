r,s=map(int,input().split())
l=list(map(int,input().split()))
l.sort(reverse=True)

q=s
ctr=0
for i in l:
    if(q>=i):
        num=int(q/i)
        ctr=ctr+num
        q=q-num*i
    if q==0:
        break
if(q==0):
   print(ctr)
else:
   print("it's not possible to select coins in such a way that they sum upto ",s)     

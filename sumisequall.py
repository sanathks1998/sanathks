r,s=map(int,input().split())
l=list(map(int,input().split()))
flag=0
for i in range(r):
    for x in range(i+1,r):
       
        if(l[i]+l[x]==s):
            flag=1
            break
        else:
            flag=0
    if(flag==1):
        break
if(flag==1):
    print("yes")
else:
    print("no")

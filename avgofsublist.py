n=int(input())
l=list(map(int,input().split()))
flag=0
q=[]
for i in range(n):
    q.append(l[i])
    w=[]
    for j in range(i+1,n):
        
        w.append(l[j])
    if(w==[]):
        w.append(0)
    
    if ((sum(q)/len(q))==(sum(w)/len(w))):
            flag=1
            break
    else:
            flag=0
            
if(flag==1):
    print("yes")
else:
    print("no")

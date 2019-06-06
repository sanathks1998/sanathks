r=int(input())
s=list(map(int,input().split()))
f=list(map(int,input().split()))
ct=[]
t=0

for i in range(r):
    ctrl=0
    t=0
    for j in range(i,r):
       
       if(s[j]>=t):
           t=f[j]
           
           ctrl=ctrl+1
    ct.append(ctrl)
print(ct)
print(max(ct)) 

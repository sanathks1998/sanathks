s=0
q=0
r=int(input())
while(r!=0):
    t=r%10
    s=s+t
    r=r//10
a=s

if(s<9):
    print("YES")
else:
    while(s!=0):
        f=s%10
        q=f+(q*10)
        
        s=s//10
    if(a==q):
        print("YES")
    else:
        print("NO")

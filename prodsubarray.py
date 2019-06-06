def mul(l):
    re=1
    for x in l:
        re=re*x
    return re   
r=int(input())
s=list(map(int,input().split()))
f=[]
f.append(mul(s))
for i in range(0,r-1):
  a=s[:i+1]
  y=s[i+1:]
  if mul(a)>mul(y):
    f.append(mul(a))
  else:
    f.append(mul(y))
print(max(f))

r=int(input())
s=list(map(int,input().split()))
f=[]
f.append(sum(s))
for i in range(0,r-1):
  a=s[:i+1]
  y=s[i+1:]
  if sum(a)>sum(y):
    f.append(sum(a))
  else:
    f.append(sum(y))
print(max(f))

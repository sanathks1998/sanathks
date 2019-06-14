r=int(input())
u=[]

q=[]
for i in range(r):
    l=[]
    l=list(map(int,input().split()))
    u.append(l)

for i in u:
    for j in i:
        q.append(j)
q.sort()

for x in q:
    print(x,end=" ")


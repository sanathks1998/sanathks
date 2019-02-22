r=int(input())
s=int(input())
l=[]
for i in range(r):
    w=int(input())
    l.append(w)
l.sort(reverse=True)
print(l[s-1])

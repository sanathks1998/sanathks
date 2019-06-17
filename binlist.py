n=int(input())
l=[]
for i in range(1,2**n):
     q=bin(i)[2::]
     l.append(q)
for x in range(1,n):
     print(l[x])

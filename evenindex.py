r=int(input())
l=list(map(int,input().split()))
y=l
while len(l)>1:
	l=l[1::2]
print(y.index(l[0]))

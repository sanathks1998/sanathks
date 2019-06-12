from itertools import combinations
s,n=map(int,input().split())
v=len(str(s))

x=list(combinations(str(s),v-n))
x=(sorted(x))

for i in x[0]:
    print(i,end=" ")


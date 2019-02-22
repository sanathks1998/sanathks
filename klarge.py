r,s=map(int,input().split())
l=list(map(int,input().split()))
l.sort(reverse=True)
print(l[s-1])

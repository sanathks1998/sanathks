r=int(input())
l=list(map(int,input().split()))
l.reverse()
for i in range(len(l)):
    if((i+1)<len(l)):
        print(l[i],end="->")
    else:
        print(l[i],end="")

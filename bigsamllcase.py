noty=int(input())
toty=list(map(int,input().split()))
r=0
for i in range(noty):
    for j in range(len(toty)):
                   if(toty[j]<toty[i]):
                       r=r+toty[j]
print(r)

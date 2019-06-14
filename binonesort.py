ovi=int(input())
rvi=list(map(int,input().split()))
fvi=gvi=[]
for i in range(0,ovi):
    fvi=list(bin(rvi[i]))
    fvi=fvi[2:]
    gvi.append(fvi)
gvi=sorted(gvi)
gvi=gvi[::-1]
for i in range(0,ovi):
    bvi=1
    zvi=0
    for j in range(len(gvi[i])-1,-1,-1):
        zvi=zvi+(int(gvi[i][j])*bvi)
        bvi=bvi*2
    print(zvi)

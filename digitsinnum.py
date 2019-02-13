nir=int(input())
rer=[]
while(nir!=0):
        fi=nir%10
        rer.append(fi)
        nir=nir//10
for xi in rer[::-1]:
        print(xi," ")


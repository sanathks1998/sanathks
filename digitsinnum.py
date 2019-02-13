ni=int(input())
re=[]
while(ni!=0):
        f=ni%10
        re.append(f)
        ni=ni//10
for x in re[::-1]:
        print(x," ")


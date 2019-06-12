n=int(input())
s=[]
y=[]
for i in  range(n):
    s.append(input().strip())
firsts=s[0]
firlen=len(firsts)

for i in range(n):
    g=s[i].find(firsts)
    if g==-1:
        clen=0
        while clen>=firlen:
            if s[i][i:clen]==s[i][i:clen]:

               clen+=1
        clen-=1
        firsts=firsts[0:clen]
        firlen=clen
print(firsts)


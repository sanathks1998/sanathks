
l=input()
t=[]
x='b'
ctr=0
if 'ab' not in l:
    print(ctr)
else:    
 for i in range(len(l)):
    ctr=1
    for j in range(i,len(l)):
        if 'a' in l[j]:
            if j+1==len(l):
                break
            elif (x==l[j+1]):
                ctr=ctr+1
        elif 'b' in l[j]:
             if j+1==len(l):
                break
             elif (x==l[j+1]):
                ctr=ctr+1
        else:
            t.append(ctr)
            ctr=1
            break
    if l[i]=='a':
        t.append(ctr)
    else:
        t.append(ctr)
 print(int(max(t)))

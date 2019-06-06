l=input()
t=[0]
x='b'
ctr=0
if 'ab' not in l:
    print(ctr)
else:    
 for i in range(len(l)):
    ctr=1
    for j in range(i,len(l)-1):
        if 'a'==l[j] and x==l[j+1]:
                ctr=ctr+1
           
        elif x==l[j] and  'a'==l[j+1]:
                ctr=ctr+1
            
        else:
            t.append(ctr)
            ctr=1
            break
    if l[i]=='a':
        t.append(ctr)
    else:
        t.append(ctr-1)
      
 print(int(max(t)))

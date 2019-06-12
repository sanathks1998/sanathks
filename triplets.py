ct=0
def trips(a,b,c):
    l=a**2
    z=b**2+c**2
    
    if l==z:
        print('a')
        return 'a'
    else:
            return 0
def ith(r,ct):
    for i in range(r):
        xth(i+1,r,i,ct)
def xth(y,b,i,ct):
    for x in range(y,b):
         jth(x+1,b,i,x,ct)
def jth(y,b,i,x,ct):
    for j in range(y,b):
            a=max(s[i],s[j],s[x])
            print(s[i]," ",s[x]," ",s[j])
            print("max is:",a)
            if(a==s[x]):
                
                r=trips(a,s[i],s[j])
                
                if(r=='a'):
                    ct+=1
            if(a==s[i]):
                
                r=trips(a,s[x],s[j])
                
                if(r=='a'):
                    ct+=1
            if(a==s[j]):
                
                r=trips(a,s[i],s[x])
                
                if(r=='a'):
                 ct+=1
   
r=int(input())
s=list(map(int,input().split()))

ith(r,ct)
print(ct)    
        
            
           


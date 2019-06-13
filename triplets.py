


   
r=int(input())
s=list(map(int,input().split()))
ct=0
for i in range(len(s)-2):
    for x in range(i+1,len(s)-1):
         for j in range(x+1,len(s)):
            if s[i]<s[x]<s[j] and i<x<j:
                ct+=1
print(ct)    
        

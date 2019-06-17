n=int(input())
l=list(map(int,input().split()))
w=[]

for i in range(n):
     q=[]
     q=l[:]
     
     if(i<n-1):
         q.remove(q[i+1])
     elif i==n-1:
          
          q.remove(q[n-2])
     elif i==0:
          q.remove(q[-1])
     if(i>0):
         q.remove(q[i-1])
     elif i==0:
          q.remove(q[-1])

     
     y=sum(q)
     w.append(y-l[i])

print(max(w))

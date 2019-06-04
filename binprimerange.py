def primes(num):
    if num > 1: 
            if(num==4):
              o=( num//2)+1
            else:
              o= num//2  
            for i in range(2,o): 
               if (num % i) == 0: 
                return 'false' 
                break
            else:
                return 'true' 
    else:
        return 'false'
       
n,k=map(int,input().split())

ctr=0
for i in range(n,k):
    t=str(bin(i))
    count=0
    for x in t:
          if(x=='1'):
           count=count+1
    if(primes(count)=='true'):
       ctr=ctr+1
print(ctr)

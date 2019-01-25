def pars(a,lows,highs): 
    i = ( lows-1 )        
    pivots = a[highs]     
    for j in range(lows , highs):
        if a[j] <= pivots: 
            i = i+1 
            a[i],a[j] = a[j],a[i] 
    a[i+1],a[highs] = a[highs],a[i+1] 
    return ( i+1 ) 
  
def qs(a,lows,highs): 
    if lows < highs: 
        pis = pars(a,lows,highs) 
        qs(a, lows, pis-1) 
        qs(a, pis+1, highs)

n=int(input("enter limit"))        
a=[int(x) for x in input().split()]  
qs(a,0,n-1)
print(a)      


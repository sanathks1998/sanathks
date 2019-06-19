
def AtBegining(l,val):
    l.insert(1,val)
def AtEnd(l,val):
   
       l.append(val)
   
def Atpos(l,val,pos):
    
        l.insert(pos-1,val)
    
def search(l,val):

    if val in l:
        return 1
       
    else:
        return 0
        
 
def delete(l):
    
        
                l.pop(0)
                return 1
       
op=1
l=[]
while(op==1):
    
    print("\n1.enquue 2.dequeue 3.peek 4.exit")
    n=int(input())
    if n==1:
            print("enter value")
            val=int(input())
            AtEnd(l,val)
   
  
                    
    elif n==3:
           if(len(l)!=0):
               print("last element is  ")
               print(l[0])
               
           else:
    
                print("empty lsit")
    
    elif n==2:
          if len(l)!=0: 
               q= delete(l)
               
               print("item deleted")
               
          else:
    
                print("empty lsit")
    
    else:
        op=0
    

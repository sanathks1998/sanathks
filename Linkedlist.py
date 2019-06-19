
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
        
 
def delete(l,val):
    
        if val<len(l):
                l.remove(l[val])
                return 1
        else:
            return 0
op=1
l=[]
while(op==1):
    
    print("\n1.insert at begining 2.insert at end,3.insert at end,4.search 5.show list 6.delete an element 7.exit")
    n=int(input())
    if n==1:
            print("enter value")
            val=int(input())
            AtBegining(l,val)
            print("inseted")
    elif n==2:
            if(len(l)!=0):
                print("enter value")
                val=int(input())
                AtEnd(l,val)
                print("inseted")
            else:
                print("empty lsit")
    elif n==3:
            if pos<len(l):
                print("enter value")
                val=int(input())
                print("enter position")
                pos=int(input())
                Atpos(l,val,pos)
                print("inseted")
            else:
                print("enter a pos less than ",len(l))
    
    elif n==4:
            if(len(l)!=0):
                print("enter value search")
                val=int(input())
                s=search(l,val)
                if s==1:
                     print("value is present")
                else:
                    
                    print("value  not is present")
            else:
                print("empty lsit")
                    
    elif n==5:
           if(len(l)!=0):
               print("elements are")
            
               for x in l:
                    print(x,end=" ")
           else:
    
                print("empty lsit")
    
    elif n==6:
            if(len(l)!=0):
               print("enter pos to delete")
               val=int(input())
               q= delete(l,val-1)
               if q==1:
                   print("item deleted")
               else:
                    print(val," not found")
            else:
    
                print("empty lsit")
    
    else:
        op=0
    

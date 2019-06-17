d=dict()
op='y' 
def add():
   
    print(" enter name of contact")
    keys=input()
    print(" add space to add another number")
    val=int(input())
    d[keys]=val
    print("contact added")
def delete():
     if d!={}:
         
         print("enter conatact name to delete")
         dels=input()
         if dels in d:
            print(dels," is deleted")
            del d[dels]
     else:
         print("no conatacts avialable")

def update():
       if d!={}:
            print("contact name to update")
            ct_name=input()
            print("press 1:update contact name, 2: to update number")
            u=int(input())
            if u==1:
                 print("entre new conatct name")
                 new_name=input()
                 d[str(new_name)]=d.pop(str(ct_name))
            if u==2:
                 print("entre new number and add space if for next number")
                 new_num=int(input())
                 d.update({ct_name:new_num})
            print("contact updated")
       else:
            print("no conatacts avialable")
def search():
        print("enter contact number")
        searc_name=input()
        if d[searc_name]:
                        print(d[searc_name])
        else:
            print("no contact listed")


                    
while(op=="y"):
     
    print("1:add,2:delete,3:update,4:search,5:see full list 6:exit")
    n=int(input())
    if(n==1):
        add()
    elif n==2:
        delete()
    elif n==3:
        update()
    elif n==6:
        op='n'
    elif n==4:
        search()
    elif n==5:
      if d!={}:
        print(d)
      else:
          print("no contacts avialable")

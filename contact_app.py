d=dict()
op='y' 
def add():
    newd={}
    print(" enter name of contact")
    keys=input()
    option=1
    while(option==1):
        print ("which fields to add 1.personal 2.work 3.email 4.desccription")
        choose=int(input())
        if(choose==1):
             print("entre details")
             num=int(input())
             newd['personal']=num
        elif(choose==2):
             print("entre details")
             num2=int(input())
             newd['work']=num2
        elif(choose==3):
             print("entre details")
             mails=input()
             newd['email']=mails
        if(choose==4):
             print("entre details")
             desc=input()
             newd['describtion']=desc
        print ("To add more press 1 else press 0")
        option=int(input())
    d[keys]=newd

   
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
        print("enter contact name")
        searc_name=input()
        if searc_name in d:
            for key,value in d.items():
             print("name :",key)
             for kid,vid in value.items():
                  print(kid,":",vid)
        else:
            print("no contact listed here are some suugestion to search insted")
            for key, value in d.items(): 
               
                if searc_name in key: 
                   print (key)


                    
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
        for key,value in d.items():
             print("name :",key)
             for kid,vid in value.items():
                  print(kid,":",vid)
      else:
          print("no contacts avialable")

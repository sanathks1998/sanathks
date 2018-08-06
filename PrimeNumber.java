import java.io.*;
import java.util.*;

public class PrimeNumber
{
  public static void main(String args[])
  {
    int f,l,i,j,c=1;
 
    Scanner sc=new Scanner(System.in);
    System.out.println("entre first interval");
    f=sc.nextInt();
    System.out.println("entre last interval");
    l=sc.nextInt();
    while(f<=l)
    {
   if(f==1)
   {
       c=0;
       
   }
       if(f==2)
       {
           c=1;
       }
   
   
      for(i=2;i<=f/2;i++)
      {
        if(f%i==0)
        {
          
          c=0;
         break;
        
    
          
        }
        else 
        {c=1;
        
        }
      }
        if(c==1)
        {
         System.out.println(f);
        }
       
    f++;    
           
      
   
  
  }
 }     
}

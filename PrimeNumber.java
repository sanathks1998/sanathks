import java.io.*;
import java.util.Scanner;

public class PrimeNumber
{
  public static void main(String args[])
  {
    int f,l,i,j,c;
 
    Scanner sc=new Scanner(System.in);
    System.out.println("entre first interval");
    f=sc.nextInt();
    System.out.println("entre last interval");
    l=sc.nextInt();
    for(j=f;j<=l;j++)
    {
        if(f==2)
        {
            System.out.println(f);
        }
        for(i=2;i<=f/2;i++)
        {
            if(f%i==0)
            {
                c=0;
                break;
            }    
          
        
        else 
        {
            c=1;
        }
        
        if (c==1)
        {
         System.out.println(f);
        } 
        
    }
    }
  
  
 }     
}  

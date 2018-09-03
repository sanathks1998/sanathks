import java.io.*;
import java.util.*;
public class ARMstronglimit
{
  public static void main(String args[])
  {
      Scanner sc=new Scanner(System.in);
    System.out.println("entre  a first limit");
      int num=sc.nextInt();
      System.out.println("entre  a second limit");
      int lst=sc.nextInt();
      int i;
      int r,sum=0,w=0;
    for(i=num;i<lst;i++)
    {
         sum=0;
        w=i;
        while(w>0)
        {
            r=w%10;
            sum=sum+r*r*r;
            w=w/10;
        }
    
      
    
        if(sum==i)
        System.out.println(i);
        
       
      }
      
      
  }}

import java.io.*;
import java.util.*;
public class ARMstrong
{
  public static void main(String args[])
  {
      Scanner sc=new Scanner(System.in);
    System.out.println("entre  a first limit");
      int num=sc.nextInt();
      int i;
      int r,sum=0;
    i=num
   while(i%10!=0)
   {
     r=i%10;
     sum=sum+r*r*r;
     i=i/10;
   }
    if(sum==num)
      System.out.println("yes");
    else
      System.out.println("no");
      
      
  }}

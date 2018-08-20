import java.io.*;
import java.util.*;
public class ARMstrong
{
  public static void main(String args[])
  {
      Scanner sc=new Scanner(System.in);
      float num=sc.nextInt();
      float i,r,sum=0;;
    if(num<=1000000)
    {
      i=num;
      while(i%10!=0)
      {
        r=i%10;
        sum=sum+(r*r*r);
        i=i/10;
      }
      if(sum==num)
      System.out.println("yes");
      
     else
      System.out.println("no");
  } }}

import java.io.*;
import java.util.*l
public class FactNum
{
  public static void main(String args[])
  {
    Scanner sc=new Scanner(System.in);
    System.out.println("entre a number");
    int a=sc.nexInt();
    int fact=0;
    for(i=1;i<=a;i++)
    {
      fact*=i;
    } 
    System.out.println(fact);
   }
 }  

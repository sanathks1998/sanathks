import java.io.*;
import java.util.*;
public class FactNum
{
  public static void main(String args[])
  {
    Scanner sc=new Scanner(System.in);
    System.out.println("entre a number");
int a=sc.nextInt();

    int fact=1,i;
    for(i=1;i<=a;i++)
    {
      fact=fact*i;
    } 
    System.out.println(fact);
   }
 } 

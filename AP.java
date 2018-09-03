import java.io.*;
import java.util.*;
public class AP
{
  public static void main(String args[])
  {
    Scanner sc=new Scanner(System.in);
   
    System.out.println("entre limit");
    int n=sc.nextInt();
 
    System.out.println("entre first element");
    int a=sc.nextInt();
    System.out.println("entre diffrence element");
    int d=sc.nextInt();
    double sum;
    double r=n/2.0;
    sum=r*((2*a)+((n-1)*d));
    System.out.println(sum);
   }
 }

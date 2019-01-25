import java.io.*;
import java.util.*;
public class MinElmnt
{
  public static void main(String args[])
  {
    Scanner sc=new Scanner(System.in);
   int min;
    System.out.println("entre limit");
    int n=sc.nextInt();
int a[]=new int[n];    
    System.out.println("entre elemnets");
    for(int i=0;i<n;i++)
     a[i]=sc.nextInt();
    min=a[0];
    
    for(int i=0;i<n;i++)
    if(min>a[i])
    {
      min=a[i];
    }
    System.out.println(min);
  }
 } 

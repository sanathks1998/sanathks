import java.io.*;
import java.util.*;
public class MaxElmnt
{
  public static void main(String args[])
  {
    Scanner 

sc=new Scanner(System.in);
   int max;
    System.out.println("entre limit");
    int n=sc.nextInt();
int a[]=new int[n];    
    System.out.println("entre elemnets");
    for(int i=0;i<n;i++)
     a[i]=sc.nextInt();
    max=a[0];
    
    for(int i=0;i<n;i++)
    if(max<a[i])
    {
      max=a[i];
    }
    System.out.println(max);
  }
 }  

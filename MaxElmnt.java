import java.io.*;
import java.util.*;
public class MaxElmnt
{
  public static void main(String args[])
  {
    Scanner sc=new Scanner(System.in);
   
    System.out.println("entre limit");
    int n=sc.nextInt();
    System.out.println("entre elemnets");
    for(int i=0;i<n;i++)
    int a[]=sc.nextInt();
    max=a[0];
    for(int i=0;i<n;i++)
    if(max<a[i])
    {
      max=a[i];
    }
    System.out.println(max);
  }
 }  

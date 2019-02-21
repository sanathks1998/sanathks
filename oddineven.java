import java.io.*;
import java.util.*;
public class Main
{
  public static void main(String args[])
  {
    Scanner sc=new Scanner(System.in);
   
   int i,j;
    int n=sc.nextInt();
 int a[]=new int[n];
 int c[]=new int[n];

   for(i=0;i<n;i++)
     a[i]=sc.nextInt();
  
   for(i=0;i<n;i++)
   
    {if(a[i]%2==0)
    {
     if(i%2!=0)
      {System.out.print(a[i]+"  ");
     }}else
      {  if(i%2==0)
       {  System.out.print(a[i]+" ");
       }}
    }    
}
 }

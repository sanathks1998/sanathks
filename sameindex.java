import java.io.*;
import java.util.*;
public class Main
{
  public static void main(String args[])
  {
    Scanner sc=new Scanner(System.in);
   
   int i,j,r;
    int n=sc.nextInt();
 int a[]=new int[n];
 int c[]=new int[n];

   for(i=0;i<n;i++)
     a[i]=sc.nextInt();
   for(i=0;i<n;i++)
   if(a[i]==i)
 
  System.out.print(a[i]+" ");
   }
 }

import java.io.*;
import java.util.*;
public class Main
{
  public static void main(String args[])
  {
    Scanner sc=new Scanner(System.in);
   
   int i,j,flag=1;
    int n=sc.nextInt();
 int a[]=new int[n];
 int c[]=new int[n];

   for(i=0;i<n;i++)
     a[i]=sc.nextInt();
     Arrays.sort(a);
   for(i=0;i<n;i++)
   {
        for(j=0;j<n;j++)
        {
            if(i!=j)
            if(a[i]!=a[j])
            {
                 flag=a[i];
            }
         }
     
     
   }     
        System.out.print(flag);
   }
 }

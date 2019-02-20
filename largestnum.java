import java.io.*;
import java.util.*;
public class Main
{
  public static void main(String args[])
  {
    Scanner sc=new Scanner(System.in);
   
   int i;
    int n=sc.nextInt();
 int a[]=new int[n];
   for(i=0;i<n;i++)
     a[i]=sc.nextInt();
   Arrays.sort(a);
   for(i=0;i<n;i++)
    System.out.print(a[i]);
   }
 }

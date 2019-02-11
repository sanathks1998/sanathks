import java.io.*;
import java.util.*;
public class Main
{
  public static void main(String args[])
  {
    Scanner sc=new Scanner(System.in);
   int avgr=0,s=0,n;
  
    int ar[]=new int[10];    
    n=sc.nextInt();
    for(int i=0;i<n;i++)
     {
      ar[i]=sc.nextInt();
      s=s+ar[i];
     }
    avgr=s/n;
    System.out.println(avgr);
   }
  }

import java.io.*;
import java.util.*;
public class Main
{
  public static void main(String args[])
  {
    Scanner sc=new Scanner(System.in);
   int maxr,smallr;
  
    int ay[]=new int[10];    
    int r=sc.nextInt();
    for(int i=0;i<r;i++)
     ay[i]=sc.nextInt();
    maxr=ay[0];
    smallr=ay[0];
    
    for(int i=0;i<n;i++)
    {
      if(maxr<ay[i])
      {
        maxi=ay[i];
      }
      if(smallr>ay[i])
      {
        smallr=ay[i];
      }
    } 
    System.out.print(smallr+" "+maxr);
  }
 }

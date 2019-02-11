import java.io.*;
import java.util.*;
public class Main
{
  public static void main(String args[])
  {
    Scanner sc=new Scanner(System.in);
   int maxr,smallr,i;
  
    int ay[]=new int[10];    
    int r=sc.nextInt();
    for( i=0;i<r;i++)
     ay[i]=sc.nextInt();
    maxr=ay[0];
    smallr=ay[0];
    
    for( i=0;i<r;i++)
    {
      if(maxr<ay[i])
      {
        maxr=ay[i];
      }
      if(smallr>ay[i])
      {
        smallr=ay[i];
      }
    } 
    System.out.print(smallr+" "+maxr);
  }
 }

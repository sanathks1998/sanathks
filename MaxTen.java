import java.io.*;
import java.util.*;
public class MaxTen
{
  public static void main(String args[])
  {
    Scanner sc=new Scanner(System.in);
   int maxi;
  
    int ar[]=new int[10];    
    
    for(int i=0;i<10;i++)
     ar[i]=sc.nextInt();
    maxi=ar[0];
    
    for(int i=0;i<10;i++)
    if(maxi<ar[i])
    {
      maxi=ar[i];
    }
    System.out.println(maxi);
  }
 }

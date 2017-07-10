#include<stdio.h>
#include<conio.h>
#include<math.h>
void main()
{
int a,i,flag=1;
clrscr();
printf("\n enter a number");
scanf("%d",&a);
for(i=2;i<=(a/2);i++ )
{
if(a%i==0)
{printf("\n %d is not prime number ",a);
flag=0;
break;
}}
if( flag==1)
printf("\n %d is a prime",a)  ;


getch();
}

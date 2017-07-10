#include<stdio.h>
#include<conio.h>
#include<math.h>
void main()
{
int a,r=0,c,s=0;
clrscr();
printf("\n enter a number");
scanf("%d",&a);
c=a;
while(a!=0)
{
r=a%10;
s=s*10+r;
a=a/10;
}
if(c==s)
printf("\n %d is pallindrome ",c);
else
printf("\n %d is not a pallindrome",c)  ;


getch();
}

#include<stdio.h>
#include<conio.h>
void main  ()
{
int a;
float i=0;
clrscr();
printf("entre a number\n");
scanf("%d",&a);
while(a%10!=0)
{
  i++;
  a=a/10;
}
printf("no of digbits is %d\n",i);
getch();
}

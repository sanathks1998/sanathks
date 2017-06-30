#include<stdio.h>
#include<conio.h>
void main  ()
{
int a;
float i=0;
clrscr();
printf("entre a number\n");
scanf("%d",&a);
while(a!=0)
{
  i++;
  a=a/10;
}
printf("no of digbits %d\n",i);
getch();
}

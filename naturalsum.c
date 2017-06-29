#include<stdio.h>
#include<conio.h>
void main()
{
int a,sum=0,i;
clrscr();
printf("entre the limit");
scanf("%d",&a);
for(i=1;i<=a;i++)
sum+=i;
printf("\n%d",sum);

getch();
}

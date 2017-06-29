#include<stdio.h>
#include<conio.h>
void main()
{
int a,;
clrscr();
printf("entre a year\n");
scanf("%d",&a);
if(a%4==0&&a%100!=0)||(a%400==0&&a%100==0)

printf("\n%d is a leap year",a);
      else
      printf("\n%d is not a leap year ",a);
getch();
}

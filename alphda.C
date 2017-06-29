#include<stdio.h>
#include<conio.h>
void main()
{
char a;
clrscr();
printf("entre a digit or alphabet\n");
scanf("%c",&a);
if((a>=65&&a<=90)||(a>=97&&a<=122))
printf("\nit is a aphabet");
      else
      printf("\nit is not a alphabet");

getch();
}

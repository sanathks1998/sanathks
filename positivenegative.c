#include<stdio.h>
#include<conio.h>
void main ()
{
  int n;
  clrscr();
  printf("entre a value");
  scanf("%d",&n);
  if(n>1)
    printf("%d",n);
  else
    printf("0");
  getch();
}

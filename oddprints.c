#include<stdio.h>
#include<conio.h>
void main()
{
int n,m;
printf("entre first limit and second limit");
scanf("%d%d",&n,&m)
do{
  if(n%2!=0)
printf("\n%d",n);
  n++;
} while(n<m);
getch();
}

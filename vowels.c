#include<stdio.h>
#include<conio.h>
void main()
{
char a;
clrscr();
printf("entre a letter:\n");
scanf("%c",&a);
if( a=='a'||a=='A'||a=='e'||a=='E'||a=='i'||a=='I'||a=='o'||a=='O'||a=='u'||a=='U')
printf("it is a vowel");
      else
      printf("it is a consonant");

getch();
}

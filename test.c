#include <stdio.h>
int main()
{
int p[15],w,k=0;
p[0]=2;
for(int i=0;i<15;i++)
{
p[i+1]=P[i]*2;
}
scanf("%d\n",&w );
for ( int j=0; j < 15; j++) {
  if (w/p[j]*1.0==1) {
    k++;
  }
}
printf("%d\n",k );






  return 0;
}

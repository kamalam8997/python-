#include<stdio.h>
int main()
{
    int num,l,r;
    scanf("%d",&num);
    scanf("%d%d",&l,&r);
    
    if((num<=l)||(num<=r))
       printf("yes");
    else
       printf("no");
    
}

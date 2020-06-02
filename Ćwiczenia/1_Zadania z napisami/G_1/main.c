#include <stdio.h>
#include <stdlib.h>
int dlugosc(char napis[])
{
    int i = 0;

    while(napis[i] != 0)
        {
            i++;
        }

    return i;
}
int foo(char nap[])
{
    int dl = dlugosc(nap);
    int zmienna = 0;
    for(int i=0;i<dl-1;i++)
        if(nap[i]==nap[i+1])
        {
            zmienna++;
        }
    return zmienna;
}
int main()
{
    char napis[100] = "aabbccddeeffgghh";
    printf("%d",foo(napis));
    return 0;
}

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
    int dl1 = dlugosc(nap);

    for(int i = dl1 - 1; i >= 0; i--)
        {
            if(!(nap[i] == nap[dl1 - i - 1]))
                {
                    return 0;
                }
        }

    return 1;
}
int main()
{
    char nap1[100] = "kajak";
    char nap2[100] = "anna";
    char nap3[100] = "park";
    printf("%d\n", foo(nap1));
    printf("%d\n", foo(nap2));
    printf("%d\n", foo(nap3));
    return 0;
}

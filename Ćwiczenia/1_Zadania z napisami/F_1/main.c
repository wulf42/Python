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
void foo(char nap1[], char nap2[])
{
    int dl1 = dlugosc(nap1);
    int dl2 = dlugosc(nap2);
    int zm = 0;

    for(int i = dl1 - 1; i >= 0; i--)
        {
            nap2[dl2 + zm] = nap1[i];
            zm += 1;
        }
}
int main()
{
    char nap1[101] = "abc";
    char nap2[201] = "uuu";

    foo(nap1, nap2);
    printf("%s %s", nap1, nap2);

    return 0;
}

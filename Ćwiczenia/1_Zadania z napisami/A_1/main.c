#include <stdio.h>
#include <stdlib.h>
void foo(char nap1[], char nap2[], char nap3[])
{
    /* Wersja */
    /* nap1 = nap1 */
    /* nap2 = nap2 + nap1 */
    /* nap3 = nap3 + nap2 */
    char temp[15];
    strcpy(temp, nap2);
    strcat(nap2, nap1);
    strcat(nap3, temp);
}
void foo2(char nap1[], char nap2[], char nap3[])
{
    /* Wersja */
    /* nap1 = nap1 */
    /* nap2 = nap2 + nap1 */
    /* nap3 = nap3 + nap2 + nap1*/
    strcat(nap2, nap1);
    strcat(nap3, nap2);
}
int dlugosc(char napis[])
{
    int i = 0;

    while(napis[i] != 0)
        {
            i++;
        }

    return i;
}
void foo3(char nap1[], char nap2[], char nap3[])
{

    /* wersja 1 bez u¿ycia bilbiotek*/
    int dl1 = dlugosc(nap1);
    int dl2 = dlugosc(nap2);
    int dl3 = dlugosc(nap3);

    for(int i = 0; i < dl2; i++)
        {
            nap3[dl3 + i] = nap2[i];
        }

    for(int i = 0; i < dl1; i++)
        {
            nap2[dl2 + i] = nap1[i];
        }
}
void foo4(char nap1[], char nap2[], char nap3[])
{
    /* wersja 2 bez u¿ycia bilbiotek*/
    int dl1 = dlugosc(nap1);
    int dl2 = dlugosc(nap2);
    int dl3 = dlugosc(nap3);

    for(int i = 0; i < dl1; i++)
        {
            nap2[dl2 + i] = nap1[i];
        }

    for(int i = 0; i < dl2 + dl1; i++)
        {
            nap3[dl3 + i] = nap2[i];
        }


}
int main()
{
    char nap1[15] = "aa";
    char nap2[15] = "bb";
    char nap3[300] = "cc";
    foo(nap1, nap2, nap3);
    printf("Wersja 1:\n");
    printf("%s\n", nap1);
    printf("%s\n", nap2);
    printf("%s\n", nap3);

    char nap4[15] = "aa";
    char nap5[15] = "bb";
    char nap6[300] = "cc";
    printf("\nWersja 2:\n");
    foo2(nap4, nap5, nap6);
    printf("%s\n", nap4);
    printf("%s\n", nap5);
    printf("%s\n", nap6);

    char nap7[15] = "aa";
    char nap8[15] = "bb";
    char nap9[300] = "cc";
    printf("\nWersja 3:\n");
    foo3(nap7, nap8, nap9);
    printf("%s\n", nap7);
    printf("%s\n", nap8);
    printf("%s\n", nap9);

    char nap10[15] = "aa";
    char nap11[15] = "bb";
    char nap12[300] = "cc";
    printf("\nWersja 4:\n");
    foo4(nap10, nap11, nap12);
    printf("%s\n", nap10);
    printf("%s\n", nap11);
    printf("%s\n", nap12);

    return 0;
}

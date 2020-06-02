#include <stdio.h>
#include <stdlib.h>
/*4. Zdefiniuj strukturê Romb,
która przechowuje d³ugoœci boków rombu. Napisz funkcjê, która przyjmuje jako parametr zmienna typu Romb i
zwraca obwód tak przekazanej figury. Stwórz przypadek testowy dla funkcji.*/
struct romb
{
    int a;
} zm1, zm2;
int funkcja(struct romb zm)
{
    return zm.a * 4;
}
int main()
{
    zm1.a = 10;
    zm2.a = 3;
    printf("%d\n", funkcja(zm1));
    printf("%d\n", funkcja(zm2));
    return 0;
}

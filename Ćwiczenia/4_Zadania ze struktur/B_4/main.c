#include <stdio.h>
#include <stdlib.h>
/*4. Zdefiniuj struktur� Romb,
kt�ra przechowuje d�ugo�ci bok�w rombu. Napisz funkcj�, kt�ra przyjmuje jako parametr zmienna typu Romb i
zwraca obw�d tak przekazanej figury. Stw�rz przypadek testowy dla funkcji.*/
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

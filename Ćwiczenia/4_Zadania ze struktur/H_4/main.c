#include <stdio.h>
#include <stdlib.h>
/*4. Zdefiniuj struktur� Siedmiokat,  kt�ra przechowuje d�ugo�ci bok�w siedmiok�ta.
Napisz funkcj�, kt�ra przyjmuje jako parametr zmienna typu Siedmiokat i zwraca obw�d tak przekazanej figury. Stw�rz przypadek testowy dla funkcji.*/
struct siedmiokat
{
    int a;
    int b;
    int c;
    int d;
    int e;
    int f;
    int g;

};
int obwod(struct siedmiokat zm)
{
    return zm.a + zm.b + zm.c + zm.d + zm.e+zm.f + zm.g;
}
int main()
{
    struct siedmiokat zm1 = {5, 1, 2, 5, 5, 2, 6};
    struct siedmiokat zm2 = {5, 5, 5, 5, 5, 5, 5};
    printf("%d\n", obwod(zm1));
    printf("%d\n", obwod(zm2));
    return 0;
}


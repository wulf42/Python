#include <stdio.h>
#include <stdlib.h>
/*Zdefiniuj struktur� Trapez,  kt�ra przechowuje d�ugo�ci bok�w trapezu.
Napisz funkcj�, kt�ra przyjmuje jako parametr zmienna typu Trapez i zwraca obw�d tak przekazanej figury. Stw�rz przypadek testowy dla funkcji.*/
struct trapez
{
    int a;
    int b;
    int c;
    int d;
};
int obwod(struct trapez zm)
{
    return zm.a + zm.b + zm.c + zm.d;
}
int main()
{
    struct trapez zm1 = {5, 1, 2, 5};
    struct trapez zm2 = {5, 5, 5, 5};
    printf("%d\n", obwod(zm1));
    printf("%d\n", obwod(zm2));
    return 0;
}

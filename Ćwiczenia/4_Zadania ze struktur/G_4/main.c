#include <stdio.h>
#include <stdlib.h>
/*4. Zdefiniuj struktur� Szesciokat,  kt�ra przechowuje d�ugo�ci bok�w sze�ciok�ta.
Napisz funkcj�, kt�ra przyjmuje jako parametr zmienna typu Szesciokat i zwraca obw�d tak przekazanej figury. Stw�rz przypadek testowy dla funkcji.*/
struct szesciokat
{
    int a;
    int b;
    int c;
    int d;
    int e;
    int f;
};
int obwod(struct szesciokat zm)
{
    return zm.a + zm.b + zm.c + zm.d + zm.e+zm.f;
}
int main()
{
    struct szesciokat zm1 = {5, 1, 2, 5, 5, 2};
    struct szesciokat zm2 = {5, 5, 5, 5, 5, 5};
    printf("%d\n", obwod(zm1));
    printf("%d\n", obwod(zm2));
    return 0;
}


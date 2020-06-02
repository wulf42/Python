#include <stdio.h>
#include <stdlib.h>
/*Zdefiniuj strukturê Trapez,  która przechowuje d³ugoœci boków trapezu.
Napisz funkcjê, która przyjmuje jako parametr zmienna typu Trapez i zwraca obwód tak przekazanej figury. Stwórz przypadek testowy dla funkcji.*/
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

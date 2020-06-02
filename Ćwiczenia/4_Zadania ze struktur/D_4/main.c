#include <stdio.h>
#include <stdlib.h>
struct planeta
{
    int numer;
    char *nazwa;
    double promien;
};
struct planeta funkcja(struct  planeta * tab)
{
    //najwiekszyy promien i jego index
    double najwiekszy = tab[0].promien;
    int index = 0;

    for(int i = 1; i < 3; i++)
        {
            if(najwiekszy < tab[i].promien)
                {
                    najwiekszy = tab[i].promien;
                    index = i;
                }
        }

    double potega = tab[index].promien * tab[index].promien * tab[index].promien;
    //najwieksza objetosc
    double obj = (4.0 / 3.0 * 3.14 * potega);
    printf("Najwieksza objetosc w formacie naukym: %e", obj);
    return *(tab + index);
}
int main()
{
    //deklaruj tablice
    struct planeta tab[1000];

    tab[0].numer = 1;
    tab[0].nazwa = "Ziemia";
    tab[0].promien = 6371.0;
    //________________________________________
    tab[1].numer = 2;
    tab[1].nazwa = "Mars";
    tab[1].promien = 3389.0;
    //________________________________________
    tab[2].numer = 3;
    tab[2].nazwa = "Jowisz";
    tab[2].promien = 69911.0;
    //________________________________________
    tab[3].numer = 4;
    tab[3].nazwa = "Saturn";
    tab[3].promien = 58232.0;
    //________________________________________
    printf("\n%d %s %lf", funkcja(tab));

    return 0;
}

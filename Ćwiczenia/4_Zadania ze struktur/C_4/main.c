#include <stdio.h>
#include <stdlib.h>
/*Zdefiniuj strukturê dane_osobowe s³u¿¹c¹ do przechowywania imienia, nazwiska i wieku.
Napisz funkcjê najmlodszy, która dostaje jako argument tablice tab struktur dane_osobowe oraz jej rozmiar i wypisuje na standardowym wyjœciu imiê i nazwisko najm³odszej spoœród osób,
której dane przechowywane s¹ w tablicy tab. Je¿eli w tablicy tab jest wiêcej takich osób, to nale¿y wypisaæ imiona i nazwiska ich wszystkich. Stwórz przypadek testowy.*/
struct dane_osobowe
{
    char *imie;
    char *nazwisko;
    int wiek;
};
void najmlodszy(struct dane_osobowe *tab, int rozmiar)
{
    int lata = tab[0].wiek;

    for(int i = 1; i < rozmiar; i++)
        {
            if(lata > tab[i].wiek)
                {
                    lata = tab[i].wiek;
                }
        }

    for(int i = 0; i < rozmiar; i++)
        {
            if(tab[i].wiek == lata)
                {
                    printf("%s %s %d\n", tab[i].imie, tab[i].nazwisko, tab[i].wiek);
                }
        }
}

int main()
{
    struct dane_osobowe tab[1000];
    tab[0].imie = "Jerzy";
    tab[0].nazwisko = "Kowalski";
    tab[0].wiek = 20;

    tab[1].imie = "Szymon";
    tab[1].nazwisko = "Baldura";
    tab[1].wiek = 21;

    tab[2].imie = "Norbert";
    tab[2].nazwisko = "Gierczak";
    tab[2].wiek = 21;

    tab[3].imie = "Jakub";
    tab[3].nazwisko = "Sajko";
    tab[3].wiek = 20;

    najmlodszy(tab, 4);
    return 0;
}



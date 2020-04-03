import os
import random
os.system('cls')
ile = int(input("Podaj górne ograniczenie zakresu: "))
a = random.sample(range(1, ile+1), 1)
a = int(a[0])
os.system('cls')
liczba = 0
proba = 0
print(f"Zgadnij liczbę od 1 do {ile}")
while(a != liczba):
    liczba = int(input())
    os.system('cls')
    proba = proba+1
    if(liczba > a):
        print(f"Podano {liczba}, szukana liczba jest MNIEJSZA")
    elif(liczba < a):
        print(f"Podano {liczba}, szukana liczba jest WIĘKSZA")
    else:
        print(f"Podano {liczba}, UDAŁO SIĘ za {proba} RAZEM")

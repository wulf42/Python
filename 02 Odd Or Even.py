liczba = int(input("Podaj liczbę: "))
if liczba % 2 == 0 and liczba % 4 != 0:
    print(f"Liczba {liczba} jest parzysta")
elif liczba % 4 == 0:
    print(f"Liczba {liczba} jest parzysta, wielokrotność 4")
else:
    print(f"Liczba {liczba} jest nieparzysta")
dzielnik = int(input("Podaj dzielnik: "))
if liczba % dzielnik == 0:
    print(f"Iloraz {liczba} : {dzielnik} jest parzysty")
else:
    print(f"Iloraz {liczba} : {dzielnik} jest nieparzysty")

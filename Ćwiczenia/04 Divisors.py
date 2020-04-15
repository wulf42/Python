liczba = int(input("Podaj liczbę: "))
x = liczba
print(f"Dzielniki liczby {liczba} to: ")
for a in range(1, liczba+1):
    if liczba % a == 0:
        x = int(liczba/a)
        print(x, end=' ')

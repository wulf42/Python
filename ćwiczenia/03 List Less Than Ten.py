a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
c = []
for liczby in a:
    if(liczby < 5):
        b.append(liczby)
print(f"liczby mniejsze niż 5: {b}")
cyfra = int(input("Podaj liczbę "))
for liczby in a:
    if(liczby < cyfra):
        c.append(liczby)
print(f"liczby mniejsze niż {cyfra}: {c}")

liczba = 10
if 0 < liczba < 11:
    print("OK")

imie = "Ariadna"
for litera in imie:
    print(litera, end="")
print()
range(5)  # start, stop step
# stop -> stop-step
print(range(5))
print(type(range(5)))
print(list(range(2, 12, 2)))
print(list(range(0, -12, -2)))
print(imie[2])
print(imie[::2])
# break idzie na koniec pętli, continue przechodzi o 1 dalej, coś jak i++

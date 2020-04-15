# Zadanie 1
print("Zadanie 1:")


class Material:
    def __init__(self, rodzaj, dlugosc, szerokosc):
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def wyswietl_nazwe(self):
        return self.rodzaj


class Ubrania(Material):
    def __init__(self, rozmiar, kolor, dla_kogo, rodzaj, dlugosc, szerokosc):
        Material.__init__(self, rodzaj, dlugosc, szerokosc)
        self.rozmiar = rozmiar
        self.kolor = kolor
        self.dla_kogo = dla_kogo

    def wyswietl_dane(self):
        return self.rozmiar, self.kolor, self.dla_kogo, self.rodzaj, self.dlugosc, self.szerokosc


class Sweter(Ubrania):
    def __init__(self, rodzaj_swetra, rozmiar, kolor, dla_kogo, dlugosc, szerokosc):
        Ubrania.__init__(self, rozmiar, kolor, dla_kogo,
                         "Sweter", dlugosc, szerokosc)
        self.rodzaj_swetra = rodzaj_swetra

    def wyswietl_dane(self):
        return self.rodzaj_swetra


ubrania = Ubrania("L", "Niebieski", "Męska", "Bluza", 100, 50)

sweter = Sweter("Bawełna", "L", "Bordowy", "Męski", 100, 50)
print(ubrania.wyswietl_dane())
print(ubrania.wyswietl_nazwe())
print(sweter.wyswietl_dane())
print(sweter.wyswietl_nazwe())


# Zadanie 2
print("Zadanie 2:")


class Kwadrat():
    def __init__(self, x):
        self.x = x
        self.y = x

    def __add__(self, bok):
        wynik = self.x+bok.x
        return wynik


def main():
    kw = Kwadrat(5)
    kw2 = Kwadrat(10)
    kw3 = kw+kw2
    print(kw3)


main()


# Zadanie 3
print("Zadanie 3:")


class Kwadrat():
    def __init__(self, x):
        self.x = x
        self.y = x

    def __gt__(self, bok):
        return self.x > bok.x

    def __ge__(self, bok):
        return self.x >= bok.x

    def __le__(self, bok):
        return self.x <= bok.x

    def __lt__(self, bok):
        return self.x < bok.x


def main():
    kw1 = Kwadrat(5)
    kw2 = Kwadrat(6)
    print(kw1 > kw2)
    print(kw1 >= kw2)
    print(kw1 <= kw2)
    print(kw1 < kw2)
    if kw1 >= kw2:
        print("Kwadrat 1 większy bądź równy Kwadrat 2")
    else:
        print("Kwadrat 1 mniejszy niż Kwadrat 2")


main()
# Zadanie 4
print("Zadanie 4:")


class Point:
    counter = []

    def __init__(self, x=0, y=0):
        """Konstruktor punktu."""
        self.x = x
        self.y = y

    def update(self, n):
        self.counter.append(n)


p1 = Point(0, 0)
p2 = Point(1, 1)
p3 = Point(1, 2)
p4 = Point(1, 3)

print(p1.counter)
p1.update(1)
print(p1.counter)
p2.update(2)
print(p2.counter)
p3.update(3)
print(p3.counter)
p4.update(4)
print(p4.counter)
# Zadanie 5
print("Zadanie 5:")


class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)


class Pracownik(Osoba):

    def __init__(self, imie, nazwisko, pensja):
        Osoba.__init__(self, imie, nazwisko)
        # lub
        # super().__init__(imie, nazwisko)
        self.pensja = pensja

    def przedstaw_sie(self):
        return f"{self.imie} {self.nazwisko} i zarabiam {self.pensja}"


class Menadzer(Pracownik):

    def przedstaw_sie(self):
        return f"{self.imie} {self.nazwisko}, jestem menadżerem i zarabiam {self.pensja}"


jozek = Pracownik("Józek", "Bajka", 2000)
adrian = Menadzer("Adrian", "Mikulski", 12000)


print(jozek.przedstaw_sie())
print(adrian.przedstaw_sie())

print(isinstance(jozek, Osoba))
print(isinstance(jozek, Menadzer))
print(isinstance(jozek, Pracownik))
print(isinstance(adrian, Osoba))
print(isinstance(adrian, Menadzer))
print(isinstance(adrian, Pracownik))


print(issubclass(Pracownik, Osoba))
print(issubclass(Osoba, Pracownik))
print(issubclass(Menadzer, Osoba))
print(issubclass(Menadzer, Pracownik))
# Zadanie 6
print("Zadanie 6:")


class Wspak:
    """Iterator zwracający wartości w odwróconym porządku"""

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


def main():
    for literki in Wspak("\nkajaki"):
        print(literki)

    kolekcja = Wspak("wyraz")
    print(kolekcja.__next__())
    print(kolekcja.__next__())
    print(kolekcja.__next__())
    print(kolekcja.__next__())
    print(kolekcja.__next__())


main()

# Zadanie 7
print("Zadanie 7:")


class Even:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        if self.index % 2 == 0:
            print(self.data[self.index])

        self.index += 1


def main():
    for literki in Even("kajaki"):
        literki
    print("\n")
    kolekcja = Even("wyraz")
    kolekcja.__next__()
    kolekcja.__next__()
    kolekcja.__next__()
    kolekcja.__next__()
    kolekcja.__next__()


main()
# Zadanie 8
print("Zadanie 8:")

class Samogloski:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if(isinstance(self.data, str)):
            if self.index >= len(self.data):
                raise StopIteration
            samogloski = ["a", "e", "i", "o", "u", "y"]
            for i in range(len(samogloski)):
                if samogloski[i] == self.data[self.index]:
                    print(self.data[self.index])
            self.index += 1

def main():
    for i in Samogloski("wyraz"):
        i


main()
# Zadanie 9
print("Zadanie 9:")


def Even(data):
    for i in range(len(data)):
        if i >= len(data):
            StopIteration
        else:
            if i % 2 == 0:
                yield data[i]


def main():
    liczby = Even("wyraz")
    print(next(liczby))
    print(next(liczby))
    print(next(liczby))

main()

# Zadanie 10
import itertools
print("Zadanie 10:")
n = [1, 2, 3, 4, 5]
x = itertools.combinations(n, 3)
i = 0
while(i != 10):
    print(next(x))
    i += 1

# Zadanie 11
print("Zadanie 11:")

def ciagf(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


ciag = ciagf(10)
for i in range(10):
    print(next(ciag))

# Zadanie 12
print("Zadanie 12:")


def Miesiace():
    Miesiace = ["Styczen", "Luty", "Marzec", "Kwiecien", "Maj", "Czerwiec",
                "Lipiec", "Sierpien", "Wrzesien", "Pazdziernik", "Listopad", "Grudzien"]
    for i in Miesiace:
        yield i


def main():
    miesiace = Miesiace()
    for i in range(12):
        print(next(miesiace))


main()

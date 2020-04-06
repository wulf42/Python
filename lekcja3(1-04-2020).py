# Zadanie 1 (Wygeneruj liczby podzielne przez 4 i zapisz je do pliku.)
print("Zadanie 3: Generuje liczby i wstawia je do pliku")
plik = open("liczby.txt", "w")
for liczba in range(1000):
    if liczba % 4 == 0:
        plik.write(f"{liczba} ")
plik.close()

# Zadanie 2 (Odczytaj plik z poprzedniego zadania i wyświetl jego zawartość w konsoli.)
print("Zadanie 2: ")
plik = open("liczby.txt", "r")
wiersze = plik.readlines()
print(wiersze)
plik.close()

# Zadanie 3 (Wykorzystując komendę with zapisz kilka linijek tekstu do pliku a następnie wyświetl je na ekranie.)
print("Zadanie 3: ")
with open("tekst.txt", "w") as plik:
    for a in range(10):
        plik.write("Przykładowy tekst zapisywany do pliku\n")
with open("tekst.txt", "r") as plik:
    for linia in plik:
        print(linia, end="")

# Zadanie 4 (Stwórz klasę NaZakupy, która będzie przechowywać atrybuty:
#   nazwa_produktu, ilosc, jednostka_miary, cena_jed oraz metody:
#   konstruktor – który nadaje wartości
#   wyświetl_produkt() – drukuje informacje o produkcie na ekranie
#   ile_produktu() – informacje ile danego produktu ma być czyli ilosc + jednostka_miary np. 1 szt., 3 kg itd.
#   ile_kosztuje() – oblicza ile kosztuje dana ilość produktu np. 3 kg ziemniaków a cena_jed wynosi 2 zł/kg wówczas funkcja powinna zwrócić wartość 3*2)
print("Zadanie 4: ")

class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc,jednostka_miary,cena_jed):
        
        self.nazwa_produktu=nazwa_produktu
        self.ilosc=ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed

    def wyświetl_produkt(self):
        return self.nazwa_produktu

    def ile_produktu(self):
        return self.ilosc, self.jednostka_miary
        

    def ile_kosztuje(self):
        return self.ilosc*self.cena_jed

     
mleko= NaZakupy("mleko",6,"l",2.99)
chleb= NaZakupy("chleb",1,"szt",2.99)
cukier= NaZakupy("cukier",3,"kg",2.99)

print(mleko.wyświetl_produkt(), mleko.ile_produktu(), mleko.ile_kosztuje())

print(chleb.wyświetl_produkt(),chleb.ile_produktu(),chleb.ile_kosztuje())

print(cukier.wyświetl_produkt(), cukier.ile_produktu(), cukier.ile_kosztuje())

 
 
 
 
# Zadanie 5
# Utwórz klasę, która definiuje ciągi arytmetyczne. Wartości powinny być przechowywane jako atrybut. Klasa powinna mieć metody:
# wyświetl_dane – drukuje elementy na ekran
# pobierz_elementy– pobiera konkretne wartości ciągu od użytkownika
# pobierz_parametry – pobiera pierwsza wartość i różnicę od użytkownika oraz ilość elementów ciągu do wygenerowania.
# policz_sume – liczy sume elementow
# policz_elementy – liczy elementy jeśli pierwsza wartość i różnica jest podana
# Stwórz instancję klasy i sprawdź działanie wszystkich metod.

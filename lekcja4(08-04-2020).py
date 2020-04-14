class Material:
    def __init__(self, rodzaj, dlugosc, szerokosc):
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def wyświetl_nazwę(self):
        return 0
    
class Ubrania:
    def __init__(self, rozmiar, kolor, dla_kogo):
        self.rozmiar = rozmiar
        self.kolor = kolor
        self.dla_kogo = dla_kogo

    def wyświetl_dane (self):
        return 0

class Sweter:
    def __init__(self, rodzaj_swetra):
        self.rodzaj_swetra = rodzaj_swetra

    def wyświetl_dane (self):
        return 0

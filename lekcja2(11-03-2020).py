# imie="Marianna"
# lista=[]
# for litera in imie:
#     lista.append(litera.upper())                słabo
# print (lista)
# print([litera.upper() for litera in imie])        #lepiej
#lista = [print(litera.upper()) for litera in imie]
# print(lista)

# suma cyfr
# liczba = 123456789
# print(sum([int(cyfra) for cyfra in str(liczba)]))

# print([2**n for n in range(5)])

# lista =[
# [1,2],
# [3,4]]

# print([element for wiersz in lista for element in wiersz if element %2==0])                                  #lepsze

# wynik=[]
# for wiersz in lista:
#     for element in wiersz:
#         if element %2==0:
#             wynik.append(element)
# print (wynik)                                                        gorsze
# imie = "Marianna"
#klucz,wartosc = (0,"M")
# {0:"M",...}
# {para[0]:para[1] for para in enumerate(imie)}
# slownik = {klucz:wartosc for klucz,wartosc in enumerate(imie)}
# slownik[0] #klucz
# print(slownik)
# slow2={0: 'M', 1: 'a', 2: 'r', 3: 'i', 4: 'a', 5: 'n', 6: 'n', 7: 'a'}
# slow_odwr={wartosc:klucz for klucz,wartosc in slownik.items()}
# print(slow_odwr)

# set
# litery=set(imie)
# print(litery)

#imie, nazwisko = ("Marian","Bąbel")
# print({*range(9)})
# from timeit import timeit
#print(timeit("{*range(9)}", number=100000))
#print(timeit("set(range(9))", number=100000))
#print(timeit("[]", number=1000000))
#print(timeit("list()", number=1000000))

# kod="""
# lista =[
# [1,2],
# [3,4]]
# wynik=[]
# [element for wiersz in lista for element in wiersz if element %2==0]
# """
#print(timeit(stmt=kod), number=1000000)


def dodaj(liczba1, liczba2):
    return liczba1 + liczba2


dodaj(2, 3)


def witaj(imie="Jan"):
    print(f'Witaj {imie}!')


witaj()
witaj("Arkadiusz")

# import start as s
# s.pow()
imie = "Malgorzata"
print(imie[0])  # pierwszy
print(imie[-1])  # ostatni
print(imie[:])  # wszystko
print(imie[-2:])  # 2 ostatnie
print(imie[::-2])
# range(start,stop,step)

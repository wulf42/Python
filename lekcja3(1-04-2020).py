#Zadanie 1
plik = open("liczby.txt","w")
for liczba in range(1000):
       if liczba%4==0:
             plik.write(f"{liczba} ")
plik.close()             

#Zadanie 2
plik = open("liczby.txt","r")
wiersze = plik.readlines()
print(wiersze)
plik.close()

#Zadanie 3
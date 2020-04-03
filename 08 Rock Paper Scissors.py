import msvcrt
import os

os.system('cls')
granie = 1
pkt1 = 0
pkt2 = 0
while (granie == 1):
    print(f" 1. Papier\n 2. Nożyce\n 3. Kamień\n Gracz 1:", end=" ")
    a = int(msvcrt.getche())
    print("\n Gracz 2:", end=" ")
    b = int(msvcrt.getche())
    os.system('cls')
    if(a == b):
        print("Remis")
    elif(a == 1 and b == 3 or a == 2 and b == 1 or a == 3 and b == 2):
        print("Wygrywa gracz 1")
        pkt1 = pkt1+1
    elif(a == 1 and b == 3 or a == 1 and b == 2 or a == 2 and b == 3):
        print("Wygrywa gracz 2")
        pkt2 = pkt2+1
    else:
        print("Podano nieprawidłową liczbę")
    print(f" Punktacja:  {pkt1} : {pkt2}\n Jeszcze raz?\n 1. Tak\n 2. Nie\n")
    granie = int(msvcrt.getche())
    os.system('cls')
if(pkt1 > pkt2):
    print(f" Wygrał gracz pierwszy mając {pkt1} pkt, gracz drugi miał ich zaledwie {pkt2}")
if(pkt1 < pkt2):
    print(f" Wygrał gracz pierwszy mając {pkt2} pkt, gracz drugi miał ich zaledwie {pkt1}")
if(pkt1 == pkt2):
    print(f" Remis {pkt1} do {pkt2}")

#   Patrycja Brodzik   dsw50708@student.dsw.edu.pl

import random
import math

#Zadanie 1
print(f"Zadanie 1: Napisz program, który wypisze liczby podzielne przez 8 ( w zakresie 1..100).\n")

liczby1 = ""
for i in range(1,100):
    if i % 8 == 0:
        liczby1 += f"{i} "
print(liczby1)


#Zadanie 2
print(f"\n\nZadanie 2: Napisz program, który wypisze na ekran liczby od zadanej wartości do zera i podzielne przez 6 oraz 9.\n")

n2 = int(input("Żądana wartość:   "))
liczby2 = ""
for i in range(n2,0,-1):
    if i % 6 == 0 and i % 9 == 0:
        liczby2 += f"{i} "
print(liczby2)


#Zadanie 3
print(f"\n\nZadanie 3: Napisz program wypisujący nieparzyste liczby z zakresu 100 do 200, ale niepodzielne przez 2 i 3.\n")

liczby3 = ""
for i in range(100,200):
    if i % 2 != 0 and i % 3 != 0:
        liczby3 += f"{i} "
print(liczby3)

#Zadanie 4
print(f"\n\nZadanie 4: Napisz program wypisujący parzyste liczby z zakresu 100 do 200, ale niepodzielne przez 5,6 i 11.\n")

liczby4 = ""
for i in range(100,200):
    if i % 5 != 0 and i % 6 != 0 and i % 11 != 0:
        liczby4 += f"{i} "
print(liczby4)

#Zadanie 5
print(f"\n\nZadanie 5: Napisz program, który wyznaczy silnię.\n")
n5 = int(input("Prosze podać n silnia:   "))

def silnia(n):
    if n > 1:
        return n*silnia(n-1)
    return 1


print(f"Silnia {n5} liczb: ")
for i in range(n5):
    print(silnia(i+1))


#Zadanie 6
print(f"\n\nZadnie 6: Napisz program wyświetlający trójkąt prostokątny z gwiazdek (*, **, *** itp.).\n")

n6 = int(input("Prosze podać podstawę trójkąta:   "))
linia6 = ""
for i in range(n6):
    for j in range(i+1):
        linia6 += "* "
    print(linia6)
    linia6 = ""


#Zadanie 7
print(f"\n\nZadanie 7: Napisz program, który wyświetli n kolejnych potęg naturalnych liczby 2.\n")

n7 = int(input("Prosze podać n:   "))
for i in range(n7):
    print(f"2 do potęgi {i+1}: {int(math.pow(2,i+1))}")


#Zadanie 8
print(f"\n\nZadanie 8: Napisz program, który wypisze największą liczbę niepodzielną przez 2,3,5,7 ale mniejszą od 1000.\n")

eight = True
liczba8 = 999

while eight == True:
    if liczba8 % 2 != 0 and liczba8 % 3 != 0 and liczba8 % 5 != 0 and liczba8 % 7 != 0:
        print(f"Największa liczba niepodzielna przez 2,3,5,7 i mniejsza niż 1000 to:   {liczba8}")
        eight = False
    else:
        liczba8 -= 1


#Zadanie 9
print(f"\n\nZadanie 9: Napisz program, który symuluje działanie „LOTTO” ")

LottoKupon = []
print("Proszę wypełnić kupon Lotto: ")
i9 = 0

while i9 < 6:
    l9 = int(input(f"{i9+1} liczba: "))
    if l9 >= 1 and l9 <= 49:
        if LottoKupon.count(l9) == 0:
            LottoKupon.append(l9)
            i9 += 1
        else:
            print("Coś poszło nie tak, proszę jeszcze raz podać liczbę!")
    else:
        print("Coś poszło nie tak, proszę jeszcze raz podać liczbę!")
LottoKupon.sort()

print(f"\nTwój kupon:   {LottoKupon}")

Lotto = []
j9 = 0

while j9 < 6:
    r = random.randint(1,49)
    if Lotto.count(r) == 0:
        Lotto.append(r)
        j9+=1
Lotto.sort()

print(f"Wylosowane liczby:   {Lotto}")


#Zadanie 10
print(f"\n\nZadanie 10: Napisz program, który symuluje działanie „Multi Multi”.\n")

MultiMultiKupon = []
ile10 = int(input("Zadecyduj, ile liczb typujesz w zakładach od 1 do 10 liczb.:   "))
print("Proszę wypełnić kupon Multi Multi: ")
i10 = 0

while i10 < ile10:
    l10 = int(input(f"{i10+1} liczba: "))
    if l10 >= 1 and l10 <= 80:
        if MultiMultiKupon.count(l10) == 0:
            MultiMultiKupon.append(l10)
            i10 += 1
        else:
            print("Coś poszło nie tak, proszę jeszcze raz podać liczbę!")
    else:
        print("Coś poszło nie tak, proszę jeszcze raz podać liczbę!")
MultiMultiKupon.sort()

print(f"\nTwój kupon:   {MultiMultiKupon}")

MultiMulti = []
j10 = 0

while j10 < 20:
    r = random.randint(1,80)
    if MultiMulti.count(r) == 0:
        MultiMulti.append(r)
        j10+=1
MultiMulti.sort()

print(f"Wylosowane liczby:   {MultiMulti}")


#Zadanie 11
print(f"\n\nZadanie 11: Napisz program, który symuluje działanie „Mini LOTTO”.\n")

MiniLottoKupon = []
print("Proszę wypełnić kupon Mini Lotto: ")
i11 = 0

while i11 < 5:
    l11 = int(input(f"{i11+1} liczba: "))
    if l11 >= 1 and l11 <= 42:
        if MiniLottoKupon.count(l11) == 0:
            MiniLottoKupon.append(l11)
            i11 += 1
        else:
            print("Coś poszło nie tak, proszę jeszcze raz podać liczbę!")
    else:
        print("Coś poszło nie tak, proszę jeszcze raz podać liczbę!")
MiniLottoKupon.sort()

print(f"\nTwój kupon:   {MiniLottoKupon}")

MiniLotto = []
j11 = 0

while j11 < 5:
    r = random.randint(1,42)
    if MiniLotto.count(r) == 0:
        MiniLotto.append(r)
        j11+=1
MiniLotto.sort()

print(f"Wylosowane liczby:   {MiniLotto}")


#Zadanie 12
print(f"\n\nZadanie 12: Napisz program, który podaje 50 razy wynik rzutu monetą - losowo 0 lub 1.\nZapamiętuj liczbę wylosowanych zer i jedynek i na koniec wyświetl podsumowanie.\nZmodyfikuj program żeby zamiast 0 lub 1 po wylosowaniu wyświetlało się 'orzeł' lub 'reszka'.\n")

ile_razy_wypadła_reszka = 0
ile_razy_wypadł_orzeł = 0

for i in range (50):
    los = random.randint(0,1)
    if los == 1:
        #print("orzeł   ")
        ile_razy_wypadł_orzeł += 1
    else:
        #print("reszka   ")
        ile_razy_wypadła_reszka += 1

print(f"\nIle razy wypadł orzeł: {ile_razy_wypadł_orzeł}"
      f"\nIle razy wypadła reszka: {ile_razy_wypadła_reszka}")

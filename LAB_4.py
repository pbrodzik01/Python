#   Patrycja Brodzik   dsw50708@student.dsw.edu.pl
import math
#Zadanie 1
print("Zadanie 1: Napisz program przy użyciu pętli while który wyświetli na ekranie 100 razy napis : To jest efekt pętli while.")

i = 0
while i < 100:
    print("To jest efekt pętli while")
    i += 1


#Zadanie 2
print(f"\n\nZadanie 2: Napisz program przy użyciu pętli while wyświetlający na ekranie liczby od 254 do 320, ale niepodzielne przez 2 ale podzielne przez 5.\n")

liczby2 = ""
i = 254
while i < 320:
    if i % 2 != 0 and i % 5 == 0:
        liczby2 += f"{i} "
    i += 1
print(liczby2)

#Zadanie 3
print(f"\n\nZadanie 3: Napisz program przy użyciu pętli while, w którym podajemy liczbę naturalną do momentu podania liczby podzielnej przez 12.\nAlgorytm kończy działanie napisem: 'Podałeś liczbę podzielną przez 12, wiec kończę działanie pętli'.\n")

status3 = True

while status3 == True:
    n3 = int(input("Prosze podać liczbę:   "))
    if n3 % 12 == 0:
        print("Podałeś liczbę podzielną przez 12, wiec kończę działanie pętli!")
        status3 = False

#Zadanie 4
print(f"\n\nZadanie 4: Napisz program przy użyciu pętli while wczytujący z klawiatury wartości,\na następnie wyświetlający średnią tych wartości, niech program kończy wprowadzanie, kiedy natrafi na cyfrę 0.")

tab4 = []
status4 = True

while status4 == True:
    i4 = int(input("\nProszę podać liczbę:   "))
    if i4 == 0:
        status4 = False
    else:
        tab4.append(i4)
        print(f"Średnia podanych wartości wynosi:   {sum(tab4)/len(tab4)}")


#Zadanie 5
print(f"\n\nZadanie 5: Napisz program przy użyciu pętli while , który skończy wczytywania liczb podawanych przez użytkownika,\ngdy ich suma przekroczy 100 albo średnia wyniesie 66.\n")

tab5 = []
status5 = True

while status5 == True:
    tab5.append(int(input("Proszę podać liczbę:   ")))

    if sum(tab5) > 100 or sum(tab5)/len(tab5) == 66:
        print("Suma lub średnia przekroczyły limit! Program został przerwany...")
        status5 = False


#Zadanie 6
print(f"\n\nZadanie 6: Napisz program, który sprawdzi, czy wpisana przez użytkownika liczba jest doskonała.\n")

def dzielniki(x):
    d = []
    for a in range(1, (int(x/2) + 1)):
        if x % a == 0:
            d.append(a)
    return d


n = int(input("Podaj liczbę   "))
suma = 0
iloczyn = 1
for i in dzielniki(n):
    suma += i
    iloczyn *= i
print ("Liczba " + str(n) + ("" if (suma == n) else " nie") + " jest liczba doskonala pierwszego stopnia")
print ("Liczba " + str(n) + ("" if (iloczyn == n) else " nie") + " jest liczba doskonala drugiego stopnia")



#Zadanie 7
print(f"\n\nZadanie 7: Sprawdź, czy podana przez użytkownika liczba jest liczbą pierwszą.\n")

def czy_pierwsza(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n7 = int(input("Proszę podac liczbę:   "))
print(czy_pierwsza(n7))


#Zadanie 8
print(f"\n\nZadanie 8: Sprawdź możliwość zastosowania pętli w zadaniu :\nPracownik przez 12 miesięcy przy zarobkach 3891 zł brutto(nie netto)odkłada co miesiąc 333zł.\nW każdym miesiącu z całej odłożonej na tą chwilę kwoty uzyskuje 8% odsetek.\nJaką kwotę zgromadzi pracownik ?\n")

skarbonka8 = 0
for i in range(12):
    skarbonka8 += 333
    skarbonka8 = skarbonka8 + round(skarbonka8 * 0.08, 2)
print(skarbonka8)


#Zadanie 9
print(f"\n\nZadanie 9: Napisz program, który wczytuje i zlicza wczytanie po kolei liczby aż do momentu,\ngdy wartośćbezwzględna różnicy pomiędzy dwoma kolejnymi liczbami będzie mniejsza od 5.\n")

status9 = True
licz9 = 0

kolejna = int(input("Proszę podać kolejną liczbę:   "))
licz9 += 1

while status9 == True:
    poprzednia = kolejna
    kolejna = int(input("Proszę podać kolejną liczbę:   "))

    if abs(poprzednia - kolejna) >= 5:
        licz9 += 1
    else:
        print(f"\nProgram przerwany...")
        print(f"Ilość wczytanych liczb:   {licz9}")
        status9 = False


#Zadanie 10
print(f"\n\nZadanie 10: Napisz program, który wczytuje i sumuje po kolei liczby aż do momentu, gdy dwie kolejne liczby będą takie same.\n")

status10 = True
suma10 = 0

kolejna = int(input("Proszę podać kolejną liczbę:   "))
suma10 += kolejna

while status10 == True:
    poprzednia = kolejna
    kolejna = int(input("Proszę podać kolejną liczbę:   "))

    if poprzednia != kolejna:
        suma10 += kolejna
    else:
        print(f"\nProgram przerwany...")
        print(f"Suma wczytanych liczb:   {suma10}")
        status10 = False
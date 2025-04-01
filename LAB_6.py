#   Patrycja Brodzik   dsw50708@student.dsw.edu.pl

import random
#Zadanie 1 i 2
print(f"Zadanie 1 i 2: Napisz program w którym zadeklarujesz w tablicy 10 dowolnych elementów liczbowych i program wypisze 1,4,7,9 element z tej tablicy.\n")

tab = []
for i in range(10):
    tab.append(random.randint(0,100))
print(f"Zadeklarowane elementy:   {tab}")
print(f"1 element:   {tab[0]};   4 element:   {tab[3]};   7 element:   {tab[6]};   9 element:   {tab[8]}")


#Zadanie 3
print(f"\n\nZadanie 3: Napisz program w którym zadeklarujesz w tablicy 10 dowolnych elementów z zakresu liczb 0-59 i dodasz 3 dowolne liczby parzyste\ndo tablicy metodą append i insert i usuniesz 3 dowolne liczby nieparzyste metodą pop i remove. Podmień 5 i 10 element tablicy na wartości 3 i 33.\n")

tab3 = []
for i in range(10):
    tab3.append(random.randint(0,59))
print(f"Zadeklarowano 10 liczb:   {tab3}")

tab3.insert(4, random.randint(1,59)*2)
tab3.append(random.randint(1,59)*2)
tab3.insert(9, random.randint(1,59)*2)
print(f"Dodano 3 liczby dodatnie:   {tab3}")

del3 = int(input("Jaką wartość mam usunąć?   "))
tab3.remove(del3)
print(f"Tablica po usunięciu elementu:   {tab3}")
del3 = int(input("Jaką wartość mam usunąć?   "))
tab3.remove(del3)
print(f"Tablica po usunięciu elementu:   {tab3}")
del3 = int(input("Jaką wartość mam usunąć?   "))
tab3.remove(del3)
print(f"Tablica po usunięciu elementu:   {tab3}")

tab3[4] = 3
tab3[9] = 33
print(f"Tablica po podmienieniu elementów:   {tab3}")


#Zadanie 4
print(f"\n\nZadanie 4: Napisz program, który jako parametr wejściowy przyjmie liczbę naturalną n.\nFunkcja powinna zwracać listę składającą się ze wszystkich dzielników liczby n.\n")

n4 = int(input("Prosze podać n: "))
tab_dzielniki = []

for i in range(1, int(n4 / 2) + 1):
    if n4 % i == 0:
        tab_dzielniki.append(i),
tab_dzielniki.append(n4)

print(f"Dzielniki liczby {n4} :   {tab_dzielniki}")


#Zadanie 5
print(f"\n\nZadanie 5: Napisz program, który wygeneruje ciąg n – liczb zadeklarowanych przez użytkownika z zakresu x do z – zadeklarowanych przez użytkownika.\nWypisz trzeci element od końca. Usuń k-element od końca(wybrany przez użytkownika). Wygeneruj drugi ciąg, który scalisz z pierwszą listą.\nSprawdź czy liczby się powtarzają. Wygeneruj długość listy oraz ilość wystąpień każdej liczby w połączonym ciągu.\n")

tab5_a = []
n5 = int(input("Proszę podać ilość liczb do wygenerowania:   "))
początek_zakresu5 = int(input("Proszę podać początek zakresu:   "))
koniec_zakresu5 = int(input("Proszę podać koniec zakresu:   "))

for i in range(n5):
    tab5_a.append(random.randint(początek_zakresu5,koniec_zakresu5))
print(f"\nWygenerowany ciąg pierwszy:   {tab5_a}")

tab5_a.reverse()
print(f"\nTrzeci element od końca:   {tab5_a[2]}")

który_usunąć = int(input(f"Który element od końca mam usunąć 1 - {n5}:   "))
tab5_a.pop(który_usunąć-1)

tab5_a.reverse()
print(f"Element usunięto, aktualny stan tablicy:   {tab5_a}")

tab5_b = []
n5_b = int(input("\nProszę podać ilość liczb do wygenerowania drugiego ciągu:   "))
początek_zakresu5_b = int(input("Proszę podać początek zakresu:   "))
koniec_zakresu5_b = int(input("Proszę podać koniec zakresu:   "))
for i in range(n5_b):
    tab5_b.append(random.randint(początek_zakresu5_b,koniec_zakresu5_b))
print(f"\nWygenerowany ciąg drugi:   {tab5_b}")

tab5 = tab5_a + tab5_b
print(f"\nTablica po scaleniu:   {tab5}")
print(f"Długość tablicy po scaleniu:   {len(tab5)}\n")
tab5.sort()

unikalne = []
powtórzenia = []

print(f"Element:   {tab5[0]}, Powtórzeń:   {tab5.count(tab5[0])}")
for i in range(1, len(tab5)):
    if tab5[i-1] == tab5[i]:
        continue
    else:
        print(f"Element:   {tab5[i]}, Powtórzeń:   {tab5.count(tab5[i])}")


#Zadanie 6
print(f"\n\nZadanie 6: Napisz program, który usunie z listy duplikaty wygenerowane z wybranego zakresu przez funkcję random,\nnastępnie wypisze na ekran ilość pozostałych elementów oraz zwróci długość list.\n")
tab6 = []
n6 = int(input("Proszę podać ilość liczb do wygenerowania:   "))
początek_zakresu = int(input("Proszę podać początek zakresu:   "))
koniec_zakresu = int(input("Proszę podać koniec zakresu:   "))

for i in range(n6):
    tab6.append(random.randint(początek_zakresu,koniec_zakresu))

print(f"\nLista wygenerowanych liczb:   {tab6}")
print(f"Długość:   {len(tab6)}")

tab6 = list(set(tab6))
tab6.sort()

print(f"\nLista po usunięciu duplikatów:   {tab6}")
print(f"Długość:   {len(tab6)}")


#Zadanie 7
print(f"\n\nZadanie 7: Napisz program typu losowanie Lotto znane z poprzednich zajęć w oparciu o funkcję random i listy.\nUżytkownik powinien do listy wpisać liczby i porównać je z liczbami w wylosowanej liście.\nUżytkownik powinien otrzymać informację ile liczb trafił, jaką nagrodę pienieżną wygrał np. 10 000 000 PLN.\nProgram powinien umożliwić np. wygenerowanie losowo liczb użytkownika przy większej ilości losów.\n")

print(f"   ***   Witaj w symulatorze gry LOTTO   ***   ")
ile_kuponów_7 = int(input("Ile kuponów chcesz wypełnić:   "))
czy_uzupełnić_7 = input("Czy mam wpełnić je za ciebie ? - YES / NO -   ")

kupony = [[0 for col in range(6)] for row in range(ile_kuponów_7)]

if czy_uzupełnić_7 == 'YES' :
    for i in range(ile_kuponów_7):
        j = 0
        while j < 6:
            los = random.randint(1,49)
            if kupony[i].count(los) == 0:
               kupony[i][j] = los
               j += 1
else:
    for i in range(ile_kuponów_7):
        j = 0
        print(f"*** KUPON {i} ***")
        while j < 6:
            los = int(input(f"{j + 1} liczba: "))
            if los >= 1 and los <= 49:
                if kupony.count(los) == 0:
                    kupony[i][j] = los
                    j += 1
                else:
                    print("Coś poszło nie tak, proszę jeszcze raz podać liczbę!")
            else:
                print("Coś poszło nie tak, proszę jeszcze raz podać liczbę!")

Lotto = []
x = 0

while x < 6:
    r = random.randint(1,49)
    if Lotto.count(r) == 0:
        Lotto.append(r)
        x+=1
Lotto.sort()

print((f"\n***   Szczęśliwe liczby   ***"))
print(Lotto)

print(f"\n***   Twoje kupony   ***")
for i in range(ile_kuponów_7):
    kupony[i].sort()
    print(kupony[i])

sprawdź_wynik = []

for i in range(ile_kuponów_7):
    ile_trafionych = 0
    for j in range(6):
        if kupony[i][j] in Lotto:
            ile_trafionych += 1
    sprawdź_wynik.append(ile_trafionych)

print(f"\nIlość trafionych liczb:   {sprawdź_wynik}")
if 3 in sprawdź_wynik:
    print("BRAWO! Trafiłeś 3 i wygrałeś Lizaka")
if 4 in sprawdź_wynik:
    print("BRAWO! Trafiłeś 4 i wygrałeś Piwo")
if 5 in sprawdź_wynik:
    print("Brawo! Trafiłeś 5 i wygrałeś miskę ryżu")
if 6 in sprawdź_wynik:
    print("BRAWO! wygrałeś worek ziemniaków")


#Zadanie 8
print(f"\n\nZadanie 8: Napisz program, który pomiesza zawartość listy wygenerowanej przez funkcję random,\na następnie te liczby posortuje w wybranej kolejności np. od najmniejszej do największej.\nWypisz zawartość listy przed i po pomieszaniu oraz sortowaniu jej elementów.\n")

tab8 = []
n8 = int(input("Proszę podać iloość elementów tablicy: "))
for i in range(n8):
    tab8.append(random.randint(1,100))

print(f"Tablica przed sortowaniem:   {tab8}")
tab8.sort()
print(f"Tablica posortowana rosnąco:   {tab8}")
random.shuffle(tab8)
print(f"Tablica po pomieszaniu:   {tab8}")
tab8.sort()
tab8.reverse()
print(f"Tablica posortowana malejąco:   {tab8}")


#Zadanie 9
print("\n\nZadanie 9: Napisz program wczytujący z klawiatury n liczb całkowitych.\nProgram ma znaleźć największą spośród podanych liczb oraz wydrukować na ekranie informację mówiącą o tym,\nile razy największa liczba wystąpiła w podanym ciągu liczb.\n")

tab9 = []
n9 = int(input("Proszę podać n:   "))
for i in range(n9):
    tab9.append(int(input(f"Podaj {i+1} liczbę:   ")))
MAX9 = max(tab9)
ILE9 = 0
for i in range(n9):
    if tab9[i] == MAX9:
        ILE9 += 1
print(f"\nNajwiększa liczba:   {MAX9}, Powtórzeń:   {ILE9}")


#Zadanie 10
print("\n\nZadanie 10:  Napisz program generujący ciąg n początkowych liczb Fibonacciego...\n")

def fib(n):
    if n == 0: return 0
    elif n == 1: return 1
    return fib(n-1) + fib(n-2)

n10 = int(input("Proszę podać liczbę:   "))
for i in range(n10):
    print(fib(i))

#Zadanie 11
print("\n\nZadanie 11: Napisz program generujący ciąg liczb pierwszych od 0 do n metoda sita Eratostanesa...\n")

def czy_pierwsza(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n11 = int(input("Proszę podać liczbę:   "))
for i in range(n11):
    if czy_pierwsza(i+1) == True:
        print(i+1)
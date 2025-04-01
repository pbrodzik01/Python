#   Patrycja Brodzik   dsw50708@student.dsw.edu.pl

import math
import random

#Zadanie 1
print(f"\n\nZadanie 1: Napisz program obliczający średnią arytmetyczną z n liczb całkowitych wprowadzonych z klawiatury\nprzy uwzględnieniu tylko liczb nieujemnych uwzględniając instrukcje continue.\n")

n1 = int(input("Proszę podać n liczb:   "))
tab1 = []

while len(tab1) < n1:
    l1 = float(input("Podaj liczbę:   "))
    if l1 > 0:
        continue
    tab1.append(l1)

print(f"\nPodane liczby:   {tab1}")
print(f"\nŚrednia arytmetyczna:   {sum(tab1)/n1}")


#Zadanie 2
print(f"\n\nZadanie 2: Napisz program uwzględniając wyrażenie break, który wypisze pierwsze 6 liczb z zadanego zakresu n do x,\na następnie przerwie działanie obliczając ich minimum, maksimum oraz średnią i medianę.\nProgram powinien przerwać również działanie w przypadku podania liczby 0 przez użytkownika.\n")

n2 = int(input("Proszę podać początek zakresu:   "))
tab2 = []

for i in range(n2,n2+6):
    if i == 0:
        break
    tab2.append(i)
print(f"Liczby:   {tab2}")
print(f"Minimum:   {min(tab2)}")
print(f"Maksimum:   {max(tab2)}")
print(f"Średnia:   {sum(tab2)/len(tab2)}")
print(f"Mediana:   {(tab2[2]+tab2[3])/2}")

#Zadanie 3
print(f"\n\nZadanie 3: Napisz program, który będzie odwracał kolejność cyfr w liczbie.\nPrzykładowo liczba 12345 w wyniku działania programu zostanie wyświetlona jako 54321.\nDodaj warunek w którym sprawdzamy, czy wczytana z klawiatury liczba jest palindromem.\n")

l3 = input("Proszę podać liczbę: ")

awers = list(l3)
rewers = awers[::-1]

print(f"Przed:   {awers}")
print(f"Po:   {rewers}")

if awers == rewers:
    print("Liczba jest palindromem!")

#Zadanie 4
print(f"\n\nZadanie 4: Napisz program w którym zapytasz użytkownika o ilość liczb (n),\nnastępnie użytkownik musi wpisać określone liczby ograniczone do ilości liczb n.\nProgram powinien po wczytaniu wyświetlić komunikat, czy liczba jest z przedziału [-6,6].\n")

n4 = int(input("Prosze podać ilość liczb:   "))
i = 0

while i < n4:
    l4 = int(input(f"\nProsze podać {i+1} liczbę:   "))
    if l4 >= -6 and l4 <= 6:
        print("Liczba jest z przedziału [-6, 6]")
    i+=1


#Zadanie 5
print(f"\n\nZadanie 5: Oblicz sumę sześcianów liczb naturalnych od 0 do 100.\n")

suma5 = 0
i5 = 0

while i5 < 101:
    suma5 += i5 ** 2
    i5 += 1
print(suma5)

print(f"\n...Rozwiń swój program, który policzy ile liczb naturalnych (od 0) trzeba zsumować, by uzyskać liczbę większą niż 10^6\n")

suma5_b = 0
i5_b = 0

while suma5_b < 10 ** 6:
    suma5_b += i5_b ** 2
    i5_b += 1
print(f"Liczba: {i5_b - 1}, Suma: {suma5_b}")


#Zadanie 6
print(f"\n\nZadanie 6: Napisz program, który będzie interpretacją gry w ”Za dużo, za mało”. Program losuje liczbę z zakresu 1...100,\na gracz (użytkownik) ma za zadanie odgadnąć,co to za liczba poprzez podawanie kolejnych wartości. Użytkownik ma 3 szanse. \n")

number6 = random.randint(1,100)
print(f"Zgadnij jaka to liczba:")

for i in range(4):
    if i < 3:
        guess = int(input(""))
        if guess > number6:
            print("Podałeś za dużą wartość")
        if guess < number6:
            print("Podałeś za małą wartość")
        if guess == number6:
            print("Gratulację!")
            break;
    else:
        print("\nHaha przegrałeś!")

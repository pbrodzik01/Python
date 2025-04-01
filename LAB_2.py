#   Patrycja Brodzik   dsw50708@student.dsw.edu.pl

import math

#Zadanie 1
print(f"Zadanie 1: Napisz program Czy liczba a jest podzielna przez b? Program ma pobrać od użytkownika dwie liczby całkowite a, b.\nJako wynik pracy program ma wydrukować informację mówiącą o tym, czy liczba a jest podzielna przez liczbę b\n(jeden z tekstów A JEST PODZIELNE PRZEZ B lub A NIE JEST PODZIELNE PRZEZ B).\n")

a_1 = int(input("Proszę podać zmienną a:   "))
b_1 = int(input("Proszę podać zmienna b:   "))

if a_1 % b_1 == 0:
    print("\nA JEST PODZIELNE PRZEZ B")
else:
    print("\nA NIE JEST PODZIELNE PRZEZ B")


#Zadanie 2
print(f"\n\nZadanie 2: Napisz program, który będzie wyświetlał komunikat, jeśli wartość zmiennej będzie mniejsza lub równa 10, inny komunikat,\njeśli wartość tej zmiennej będzie większa od 10, lecz mniejsza lub równa 25 oraz jeszcze inny komunikat, kiedy wartość ta będzie większa od 25.\n")
zmienna_2 = int(input("Proszę podać wartość zmiennej:   "))

if zmienna_2 <= 10:
    print(f"\nzmienna <= 10")
elif zmienna_2 > 10 and zmienna_2 <= 25:
    print(f"\n10 < zmienna <= 25")
else:
    print(f"\n25 < zmienna")


#Zadanie 3
print(f"\n\nZadanie 3: Napisz program, który porówna ze sobą 3 liczby i wskaże, która jest większa i czy liczby są identyczne.\nZastanów się nad opcją zagnieżdżania ifów.\n")

a_3 = int(input("Proszę podać zmienną a:   "))
b_3 = int(input("Proszę podać zmienną b:   "))
c_3 = int(input("Proszę podać zmienną c:   "))

if a_3 == b_3 == c_3:
    print("Zmienne są takie same")
else:
    if a_3 == b_3:
        if a_3 > c_3:
            print(f"\na oraz b ({a_3}) są większe niż c ({c_3})")
        else:
            print(f"\na oraz b ({a_3}) są mniejsze niż c ({c_3})")
    elif a_3 == c_3:
        if a_3 > b_3:
            print(f"\na oraz c ({a_3}) są większe niż b ({c_3})")
        else:
            print(f"\na oraz c ({a_3}) są mniejsze niż b ({c_3})")
    elif b_3 == c_3:
        if b_3 > a_3:
            print(f"\nb oraz c ({b_3}) są większe niż a ({a_3})")
        else:
            print(f"\nb oraz c ({b_3}) są mniejsze niż a ({a_3})")
    else:
        if a_3 > b_3 and a_3 > c_3:
            if b_3 > c_3:
                print(f"\na ({a_3}) jest większe niż b ({b_3}) i c ({c_3}), oraz b ({b_3}) jest większe niż c ({c_3})")
            else:
                print(f"\na ({a_3}) jest większe niż b ({b_3}) i c ({c_3}), oraz c ({c_3}) jest większe niż b ({b_3})")
        if b_3 > a_3 and b_3 > c_3:
            if a_3 > c_3:
                print(f"\nb ({b_3}) jest większe niż a ({a_3}) i c ({c_3}), oraz a ({a_3}) jest większe niż c ({c_3})")
            else:
                print(f"\nb ({b_3}) jest większe niż a ({a_3}) i c ({c_3}), oraz c ({c_3}) jest większe niż a ({a_3})")
        if c_3 > a_3 and c_3 > b_3:
            if a_3 > b_3:
                print(f"\nc ({c_3}) jest większe niż a ({a_3}) i b ({b_3}), oraz a ({a_3}) jest większe niż b ({b_3})")
            else:
                print(f"\nc ({c_3}) jest większe niż a ({a_3}) i b ({b_3}), oraz b ({b_3}) jest większe niż a ({a_3})")


#Zadanie 4
print(f"\n\nZadanie 4:  Napisz program, który wypisze czy podana liczba jest ujemna czy dodatnia oraz czy jest podzielna przez 2 z resztą.\nZaproponuj odpowiednie warunki.\n")

a_4 = int(input("Proszę podać liczbę:   "))

if a_4 == 0:
    print("\n!Liczba 0 nie jest ani dodatnia, ani ujemna!")
else:
    if a_4 > 0:
        print("\nLiczba jest dodatnia")
    else:
        print("\nLiczba jest ujemna")

    if a_4 % 2 != 0:
        print("Liczba jest podzielna przez 2 z resztą")


#Zadanie 5
print(f"\n\nZadanie 5: Napisz program „symulator badania alkomatem”, który po podaniu odpowiednich wartości w wydychanym powietrzu\n(zgodnie z przepisami prawa) wskaże stan nietrzeźwości i stan po użyciu alkoholu zgodnie z przepisami prawa.\n")

stężenie_w_wydychanym_powietrzu = float(input("Proszę podać wartość stężenia alkoholu w wydychanym powietrzu:   "))

if (stężenie_w_wydychanym_powietrzu > 0.25):
    print("\n!STAN NIETRZEŹWOŚCI!\n"
          "zawartość alkoholu w 1 dm^3 wydychanego powietrza przekracza 0,25 mg")
elif (stężenie_w_wydychanym_powietrzu >= 0.1) and (stężenie_w_wydychanym_powietrzu <= 0.25):
    print("\n!STAN PO UŻYCIU ALKOHOLU!\n"
          "zawartość alkoholu w 1 dm^3 wydychanego powietrza od 0,1 mg do 0,25 mg")
else:
    print("\nStężenie alkoholu w wydychanym powietrzu wynosi 0,0 mg")


#Zadanie 6
print(f"\n\nZadanie 6: Napisz program, który spośród czterech podanych przez użytkownika liczb wybierze największą z nich i wypisze ją na ekranie.\nSpróbuj przewidzieć wszystkie trudne kombinacje liczb a,b,c i d. Czy może być problem w którymś z przypadków?\n")

a_6 = int(input("Proszę podać pierwszą liczbę:   "))
b_6 = int(input("Proszę podać drugą liczbę:   "))
c_6 = int(input("Proszę podać trzecią liczbę:   "))
d_6 = int(input("Proszę podać czwartą liczbę:   "))

MAX = a_6

if b_6 > MAX:
    MAX = b_6
if c_6 > MAX:
    MAX = c_6
if d_6 > MAX:
    MAX = d_6

print(f"\nNajwiększą z pośród podanych liczb jest:   {MAX}")


#Zadanie 7
print(f"\n\nZadanie 7: Napisz program potrafiący rozwiązywać równanie kwadratowe: y = ax2 + bx + c\n")

a_7 = int(input("Proszę podać wartość parametru a:   "))
b_7 = int(input("Proszę podać wartość parametru b:   "))
c_7 = int(input("Proszę podać wartość parametru c:   "))

if a_7 == 0:
    print("\nTo nie jest równanie kwadratowe tylko liniowe!")
else:
    delta = (b_7 ** 2) - (4 * a_7 * c_7)

    if delta < 0:
        print("\nBrak rozwiązań w zbiorze liczb rzeczywistych!")
    elif delta == 0:
        x_0 = -b_7 / 2 * a_7
        print(f"\nIstnieje jedno rozwiązanie,\n"
              f"x_0:   {x_0}")
    else:
        x_1 = (-b_7 + math.sqrt(delta)) / 2 * a_7
        x_2 = (-b_7 - math.sqrt(delta)) / 2 * a_7
        print(f"\nIstnieją dwa rozwiązania,\n"
              f"x_1:   {x_1}\n"
              f"x_2:   {x_2}")



#Zadanie 8
print(f"\n\nZadanie 8: Napisz program, który poprosi o podanie trzech długości boków trójkąta i sprawdzi czy jest on prostokątny\n")

a_8 = int(input("Proszę podać długość boku a:   "))
b_8 = int(input("Proszę podać długość boku b:   "))
c_8 = int(input("Proszę podać długość boku c:   "))

if ((a_8 + b_8 > c_8) and (a_8 + c_8 > b_8) and (b_8 + c_8 > a_8)):
    if ((a_8**2 + b_8**2 == c_8**2) or (a_8**2 + c_8**2 == b_8**2) or (b_8**2 + c_8**2 == a_8**2)):
        print("\nTo jest trójkąt prostokątny")
    else:
        print("\nTo nie jest trójkąt prostokątny")
else:
    print("\nNie można zbudować trójkąta!")

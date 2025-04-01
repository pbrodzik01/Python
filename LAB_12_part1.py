#   Patrycja Brodzik   dsw50708@student.dsw.edu.pl

import math

def zadanie1():
    print("\n*** ZADANIE 1 ***")

    # pobieranie liczb od użytkownika
    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę: "))

    # obliczanie wyników
    suma = a + b
    roznica = a - b
    iloczyn = a * b
    if b != 0:
        iloraz = a / b
    else:
        iloraz = "Nie można dzielić przez zero!"
    pierwiastek_a = math.sqrt(a)
    pierwiastek_b = math.sqrt(b)

    # wyświetlanie wyników
    print("Suma:", suma)
    print("Różnica:", roznica)
    print("Iloczyn:", iloczyn)
    print("Iloraz:", iloraz)
    print("Pierwiastek z a:", pierwiastek_a)
    print("Pierwiastek z b:", pierwiastek_b)

def zadanie2():
    print("\n*** ZADANIE 2 ***")

    # funkcja obliczająca pole i objętość kuli
    def kula(r):
        pole = 4 * math.pi * r ** 2
        objetosc = 4 / 3 * math.pi * r ** 3
        return (pole, objetosc)

    # funkcja obliczająca pole i objętość stożka
    def stozek(r, h):
        l = math.sqrt(r ** 2 + h ** 2)
        pole = math.pi * r ** 2 + math.pi * r * l
        objetosc = 1 / 3 * math.pi * r ** 2 * h
        return (pole, objetosc)

    # funkcja obliczająca pole i objętość sześcianu
    def szescian(a):
        pole = 6 * a ** 2
        objetosc = a ** 3
        return (pole, objetosc)

    # pobieranie danych od użytkownika
    figura = input("Wybierz figurę (kula, stożek, sześcian): ")

    if figura == "kula":
        r = float(input("Podaj promień kuli: "))
        wynik = kula(r)
        print("Pole kuli:", wynik[0])
        print("Objętość kuli:", wynik[1])

    elif figura == "stożek":
        r = float(input("Podaj promień podstawy stożka: "))
        h = float(input("Podaj wysokość stożka: "))
        wynik = stozek(r, h)
        print("Pole stożka:", wynik[0])
        print("Objętość stożka:", wynik[1])

    elif figura == "sześcian":
        a = float(input("Podaj długość boku sześcianu: "))
        wynik = szescian(a)
        print("Pole sześcianu:", wynik[0])
        print("Objętość sześcianu:", wynik[1])

    else:
        print("Nieprawidłowa figura!")

def zadanie3():
    print("\n*** ZADANIE 3 ***")

    # pobieranie wysokości w stopach od użytkownika
    wysokosc_stopy = float(input("Podaj wysokość w stopach: "))

    # przeliczanie na metry, centymetry, milimetry i kilometry
    wysokosc_metry = wysokosc_stopy * 0.3048
    wysokosc_centymetry = wysokosc_metry * 100
    wysokosc_milimetry = wysokosc_centymetry * 10
    wysokosc_kilometry = wysokosc_metry / 1000

    # wyświetlanie wyników
    print("Wysokość w metrach:", wysokosc_metry)
    print("Wysokość w centymetrach:", wysokosc_centymetry)
    print("Wysokość w milimetrach:", wysokosc_milimetry)
    print("Wysokość w kilometrach:", wysokosc_kilometry)

def zadanie4():
    print("\n*** ZADANIE 4 ***")

    wysokość_w_metrach = int(input("Na jakiej wysokości lecimy? [w metrach]: "))
    wysokość_w_kilometrach = wysokość_w_metrach / 1000

    if wysokość_w_metrach < 5000:
        print(str(wysokość_w_kilometrach) + " km to za nisko!")
    else:
        print("Na tej wysokości jesteś już bezpieczny")

def zadanie5():
    print("\n *** ZADANIE 5 ***")
    def bmi(masa, wzrost):
        bmi = masa / (wzrost ** 2)

        if bmi < 18.5:
            print("Masz niedowagę")
        elif bmi >= 18.5 and bmi <= 24.99:
            print("Twoja waga jest prawidłowa")
        else:
            print("Masz nadwagę!!!")

        return bmi

    masa = float(input("Podaj masę w kg: "))
    wzrost = float(input("Podaj wzrost w m: "))
    print("TWOJE BMI WYNOSI: ", bmi(masa,wzrost))

def zadanie6():
    print("\n*** ZADANIE 6 ***")

    def convert(number, base):
        if base == "bin":
            return bin(number)[2:]
        elif base == "oct":
            return oct(number)[2:]
        elif base == "hex":
            return hex(number)[2:]
        else:
            return "Invalid base"

    def reverse_convert(number, base):
        if base == "bin":
            return int(number, 2)
        elif base == "oct":
            return int(number, 8)
        elif base == "hex":
            return int(number, 16)
        else:
            return "Invalid base"

    while True:
        print("\n1. Konwersja z dziesiętnego")
        print("2. Konwersja na dziesiętny")
        print("0. Wyjście do menu głównego")

        try:
            wybor = int(input("Proszę wybrać opcję: "))

            if wybor == 0:
                break
            elif wybor == 1:
                number = int(input("Prosze podać liczbę dziesiętną: "))
                base = input("Proszę wybrać bazę (bin, oct, hex): ")
                print("Liczba po konwersji:",convert(number, base))
            elif wybor == 2:
                number = input("Proszę podać ciąg znaków: ")
                base = input("Proszę wybrać bazę (bin, oct, hex): ")
                print("Liczba po konwersji:",reverse_convert(number, base))
            else:
                print("NIEPRAWIDŁOWY WYBÓR!")
        except ValueError:
            print("NIEPRAWIDŁOWY WYBÓR!")

def zadanie7():
    print("\n*** ZADANIE 7 ***")

    def liczba_dziesietna_na_rzymska(liczba):
        # słownik z wartościami odpowiadającymi liczbom rzymskim
        rzymskie = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX",
                    5: "V", 4: "IV", 1: "I"}

        wynik = ""
        for wartosc, symbol in rzymskie.items():
            while liczba >= wartosc:
                wynik += symbol
                liczba -= wartosc
        return wynik

    def liczba_rzymska_na_dziesietna(liczba):
        # słownik z wartościami odpowiadającymi liczbom rzymskim
        rzymskie = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9,
                    "V": 5, "IV": 4, "I": 1}

        wynik = 0
        i = 0
        while i < len(liczba):
            if i + 1 < len(liczba) and liczba[i:i + 2] in rzymskie:
                wynik += rzymskie[liczba[i:i + 2]]
                i += 2
            else:
                wynik += rzymskie[liczba[i]]
                i += 1
        return wynik

    while True:
        print("\n1. Dziesiętny -> Rzymski")
        print("2. Rzymski -> Dziesiętny")
        print("0. Wyjście do menu głównego")

        try:
            wybor = int(input("Proszę wybrać opcję: "))

            if wybor == 0:
                break
            elif wybor == 1:
                liczba_dziesiętna = int(input("Podaj liczbę w systemie dziesiętnym:   "))
                liczba_rzymska = liczba_dziesietna_na_rzymska(liczba_dziesiętna)
                print(f"Liczba dziesiętna {liczba_dziesiętna} w zapisie rzymskim to {liczba_rzymska}")
            elif wybor == 2:
                liczba_rzymska = input("Podaj liczbę w systemie rzymskim:   ")
                liczba_dziesiętna = liczba_rzymska_na_dziesietna(liczba_rzymska)
                print(f"Liczba rzymska {liczba_rzymska} w zapisie dziesiętnym to {liczba_dziesiętna}")
            else:
                print("NIEPRAWIDŁOWY WYBÓR")
        except ValueError:
            print("NIEPRAWIDŁOWY WYBÓR")


while True:
    print("\n\nLABORATORIUM 12 part 1 - PATRYCJA BRODZIK")
    print("1 - Zadanie 1")
    print("2 - Zadanie 2")
    print("3 - Zadanie 3")
    print("4 - Zadanie 4")
    print("5 - Zadanie 5")
    print("6 - Zadanie 6")
    print("7 - Zadanie 7")
    print("0 - Wyjście z programu")

    try:
        wybor = int(input("Wybierz opcję: "))

        if wybor == 0:
            break
        elif wybor == 1:
            zadanie1()
        elif wybor == 2:
            zadanie2()
        elif wybor == 3:
            zadanie3()
        elif wybor == 4:
            zadanie4()
        elif wybor == 5:
            zadanie5()
        elif wybor == 6:
            zadanie6()
        elif wybor == 7:
            zadanie7()
        else:
            print("Nieprawidłowy wybór. Wybierz opcję od 0 do 7.")
    except ValueError:
        print("Nieprawidłowy wybór. Wybierz opcję od 0 do 7.")
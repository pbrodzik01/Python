#   Patrycja Brodzik   dsw50708@student.dsw.edu.pl

def zadanie1():
    class Pojazd:
        def __init__(self):
            self.nr_tablica = None
            print("Tworzę obiekt klasy Pojazd")

        def __del__(self):
            print("Usuwanie obiektu klasy Pojazd")

    class Samochod(Pojazd):
        def __init__(self, marka, model, nr_rej):
            super().__init__()
            self.marka = marka
            self.model = model
            self.nr_tablica = nr_rej
            print(f"Tworzę samochód {self.marka} {self.model} z numerem rejestracyjnym {self.nr_tablica}")

        def jazda(self):
            print("Jadę samochodem")

    class Motocykl(Pojazd):
        def __init__(self, marka, model, nr_rej):
            super().__init__()
            self.marka = marka
            self.model = model
            self.nr_tablica = nr_rej
            print(f"Tworzę motocykl {self.marka} {self.model} z numerem rejestracyjnym {self.nr_tablica}")

        def wheelie(self):
            print("Robię na motocyklu stópkę")


    samochod = Samochod("Fiat", "Panda", "KR12345")
    samochod.jazda()

    motocykl = Motocykl("Honda", "CBR", "WAW9876")
    motocykl.wheelie()

    del samochod
    del motocykl

def zadanie2():
    class Zwierze:
        def __init__(self, imie, wiek):
            self.imie = imie
            self.wiek = wiek

        def daj_glos(self):
            pass

        def poruszaj_sie(self):
            print("Poruszam się\n")

    class Kot(Zwierze):
        def __init__(self, imie, wiek):
            super().__init__(imie, wiek)
            self.rasa = None

        def daj_glos(self):
            print("Miał\n")

        def drap(self):
            print("Drapie meble\n")

    class Pies(Zwierze):
        def __init__(self, imie, wiek):
            super().__init__(imie, wiek)
            self.rasa = None

        def daj_glos(self):
            print("Hau\n")

        def aportuj(self):
            print("Aportuję piłkę\n")

    class Ptak(Zwierze):
        def __init__(self, imie, wiek):
            super().__init__(imie, wiek)
            self.gatunek = None

        def daj_glos(self):
            print("Ćwir, ćwir\n")

        def latam(self):
            print("Latam\n")

    class Ryba(Zwierze):
        def __init__(self, imie, wiek):
            super().__init__(imie, wiek)
            self.gatunek = None

        def daj_glos(self):
            print("Nie mogę dać głosu, bo nie mam płuc\n")

        def plywam(self):
            print("Pływam\n")

    kot = Kot("Mruczek", 3)
    kot.daj_glos()  # Miał
    kot.drap()  # Drapie meble

    pies = Pies("Burek", 5)
    pies.daj_glos()  # Hau
    pies.aportuj()  # Aportuję piłkę

    ptak = Ptak("Wróbel", 1)
    ptak.daj_glos()  # Ćwir, ćwir
    ptak.latam()  # Latam

    ryba = Ryba("Karp", 2)
    ryba.daj_glos()  # Nie mogę dać głosu, bo nie mam płuc
    ryba.plywam()  # Pływam


def zadanie3():
    import math

    class Figura:
        def oblicz_obwod(self):
            pass

        def oblicz_pole(self):
            pass

    class Kwadrat(Figura):
        def __init__(self, bok):
            self.bok = bok

        def oblicz_obwod(self):
            return 4 * self.bok

        def oblicz_pole(self):
            return self.bok ** 2

    class Prostokat(Figura):
        def __init__(self, bok_a, bok_b):
            self.bok_a = bok_a
            self.bok_b = bok_b

        def oblicz_obwod(self):
            return 2 * (self.bok_a + self.bok_b)

        def oblicz_pole(self):
            return self.bok_a * self.bok_b

    class Trojkat(Figura):
        def __init__(self, bok_a, bok_b, bok_c):
            self.bok_a = bok_a
            self.bok_b = bok_b
            self.bok_c = bok_c

        def oblicz_obwod(self):
            return self.bok_a + self.bok_b + self.bok_c

        def oblicz_pole(self):
            p = self.oblicz_obwod() / 2
            return math.sqrt(p * (p - self.bok_a) * (p - self.bok_b) * (p - self.bok_c))

    class Kolo(Figura):
        def __init__(self, promien):
            self.promien = promien

        def oblicz_obwod(self):
            return 2 * math.pi * self.promien

        def oblicz_pole(self):
            return math.pi * self.promien ** 2

    class Romb(Figura):
        def __init__(self, bok, wysokosc):
            self.bok = bok
            self.wysokosc = wysokosc

        def oblicz_obwod(self):
            return 4 * self.bok

        def oblicz_pole(self):
            return self.bok * self.wysokosc

    class Trapez(Figura):
        def __init__(self, podstawa_a, podstawa_b, wysokosc):
            self.podstawa_a = podstawa_a
            self.podstawa_b = podstawa_b
            self.wysokosc = wysokosc

        def oblicz_obwod(self):
            return self.podstawa_a + self.podstawa_b + 2 * math.sqrt(
                (self.podstawa_b - self.podstawa_a) ** 2 + self.wysokosc ** 2)

        def oblicz_pole(self):
            return (self.podstawa_a + self.podstawa_b) * self.wysokosc / 2

    # pobieranie danych od użytkownika
    typ_figury = input("Podaj typ figury (kwadrat, prostokat, trojkat, kolo, romb, trapez): ")

    if typ_figury == "kwadrat":
        bok = float(input("Podaj długość boku: "))
        figura = Kwadrat(bok)
    elif typ_figury == "prostokat":
        bok_a = float(input("Podaj długość boku a: "))
        bok_b = float(input("Podaj długość boku b: "))
        figura = Prostokat(bok_a, bok_b)
    elif typ_figury == "trojkat":
        bok_a = float(input("Podaj długość boku a: "))
        bok_b = float(input("Podaj długość boku b: "))
        bok_c = float(input("Podaj długość boku c: "))
        figura = Trojkat(bok_a, bok_b, bok_c)
    elif typ_figury == "kolo":
        promien = float(input("Podaj promień: "))
        figura = Kolo(promien)
    elif typ_figury == "romb":
        bok = float(input("Podaj długość boku: "))
        wysokosc = float(input("Podaj wysokość: "))
        figura = Romb(bok, wysokosc)
    elif typ_figury == "trapez":
        podstawa_a = float(input("Podaj długość podstawy a: "))
        podstawa_b = float(input("Podaj długość podstawy b: "))
        wysokosc = float(input("Podaj wysokość: "))
        figura = Trapez(podstawa_a, podstawa_b, wysokosc)
    else:
        print("Nieznany typ figury.")
        exit()

    # obliczanie i wyświetlanie wyników
    print("Obwód:", figura.oblicz_obwod())
    print("Pole:", figura.oblicz_pole())


while True:
    print("\n\nLABORATORIUM 14 - PATRYCJA BRODZIK")
    print("1 - Zadanie 1")
    print("2 - Zadanie 2")
    print("3 - Zadanie 3")
    print("0 - Wyjście z programu")

    try:
        choose = int(input("Proszę wybrać opcję: "))

        if choose == 0:
            break
        elif choose == 1:
            zadanie1()
        elif choose == 2:
            zadanie2()
        elif choose == 3:
            zadanie3()
        else:
            print("Nieprawidłowy wybór. Wybierz opcję od 0 do 3.")
    except ValueError:
        print("Nieprawidłowy wybór. Wybierz opcję od 0 do 3.")
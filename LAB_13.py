#   Patrycja Brodzik   dsw50708@student.dsw.edu.pl

def zadanie1():
    print("\n*** ZADANIE 1 ***")
    class Samochod:
        def __init__(self, marka, model, przebieg, kolor, rodzaj, wartosc):
            self.marka = marka
            self.model = model
            self.przebieg = przebieg
            self.kolor = kolor
            self.rodzaj = rodzaj
            self.wartosc = wartosc

        def jedz_prosto(self):
            print(f"{self.marka} {self.model} jedzie prosto.")

        def skrec_w_lewo(self):
            print(f"{self.marka} {self.model} skręca w lewo.")

        def skrec_w_prawo(self):
            print(f"{self.marka} {self.model} skręca w prawo.")

        def zatrzymaj_sie(self):
            print(f"{self.marka} {self.model} zatrzymuje się.")

        def podaj_wartosc(self):
            print(f"{self.marka} {self.model} ma wartość {self.wartosc} zł.")

    # Przykładowe obiekty samochodów
    ferrari = Samochod("Ferrari", "XYZ", 10000, "czerwony", "kabriolet", 60000)
    bmw = Samochod("BMW", "X3", 50000, "czarny", "SUV", 90000)
    mercedes = Samochod("Mercedes-Benz", "C-Class", 80000, "biały", "sedan", 120000)
    audi = Samochod("Audi", "A4", 75000, "srebrny", "sedan", 95000)
    volkswagen = Samochod("Volkswagen", "Golf", 30000, "niebieski", "hatchback", 45000)

    # Przykładowe wywołanie metod na obiektach
    ferrari.jedz_prosto()
    bmw.skrec_w_lewo()
    mercedes.skrec_w_prawo()
    audi.zatrzymaj_sie()
    volkswagen.podaj_wartosc()


def zadanie2():
    class Ksiazka:
        def __init__(self, autor, tytul, rok_wydania, liczba_stron, cena):
            self.autor = autor
            self.tytul = tytul
            self.rok_wydania = rok_wydania
            self.liczba_stron = liczba_stron
            self.cena = cena

        def czytaj(self):
            print(f"Książka {self.tytul} autorstwa {self.autor} jest teraz czytana.\n")

        def podaj_cene(self):
            print(f"Cena książki {self.tytul} to {self.cena} zł.\n")

        def podaj_rok_wydania(self):
            print(f"Książka {self.tytul} została wydana w {self.rok_wydania} roku.\n")

        def podaj_autora(self):
            print(f"Autor książki {self.tytul} to {self.autor}.\n")

        def podaj_liczbe_stron(self):
            print(f"Książka {self.tytul} ma {self.liczba_stron} stron.\n")

    # Tworzenie listy książek
    ksiazki = [
        Ksiazka("J.K. Rowling", "Harry Potter i Kamień Filozoficzny", 1997, 223, 29.99),
        Ksiazka("Dan Brown", "Kod Leonarda da Vinci", 2003, 539, 39.99),
        Ksiazka("George Orwell", "Rok 1984", 1949, 328, 19.99),
        Ksiazka("Agatha Christie", "Dziesięciu Murzynków", 1939, 272, 24.99),
        Ksiazka("Stephen King", "To", 1986, 1156, 49.99)
    ]

    # Wywoływanie metod na obiektach książek
    ksiazki[0].czytaj()
    ksiazki[1].podaj_cene()
    ksiazki[2].podaj_rok_wydania()
    ksiazki[3].podaj_autora()
    ksiazki[4].podaj_liczbe_stron()

    # Sortowanie listy książek
    ksiazki.sort(key=lambda x: x.tytul)
    print("Książki posortowane alfabetycznie według tytułu:")
    for ksiazka in ksiazki:
        print(ksiazka.tytul)

    ksiazki.sort(key=lambda x: x.rok_wydania)
    print("\nKsiążki posortowane chronologicznie według roku wydania:")
    for ksiazka in ksiazki:
        print(f"{ksiazka.tytul} ({ksiazka.rok_wydania})")


def zadanie3():
    class Smartfon:
        def __init__(self, marka, model, rok_produkcji, pojemnosc_baterii, cena):
            self.marka = marka
            self.model = model
            self.rok_produkcji = rok_produkcji
            self.pojemnosc_baterii = pojemnosc_baterii
            self.cena = cena

        def uruchom_aplikacje(self, aplikacja):
            print(f"Uruchamianie aplikacji {aplikacja} na smartfonie {self.marka} {self.model}...\n")

        def pobierz_plik(self, url):
            print(f"Pobieranie pliku z adresu {url} na smartfonie {self.marka} {self.model}...\n")

        def sprawdz_pojemnosc_baterii(self):
            print(f"Pojemność baterii w smartfonie {self.marka} {self.model} wynosi {self.pojemnosc_baterii} mAh.\n")

        def podaj_rok_produkcji(self):
            print(f"Smartfon {self.marka} {self.model} został wyprodukowany w {self.rok_produkcji} roku.\n")

        def czy_wartosc(self, wartosc):
            if wartosc <= self.cena:
                print(f"Wartość {wartosc} zł jest mniejsza lub równa cenie smartfona {self.marka} {self.model}.\n")
            else:
                print(f"Wartość {wartosc} zł jest większa niż cena smartfona {self.marka} {self.model}.\n")

    # Tworzenie obiektów smartfonów
    iphone = Smartfon("Apple", "iPhone 12", 2020, 2815, 4499)
    galaxy = Smartfon("Samsung", "Galaxy S21", 2021, 4000, 3999)
    oneplus = Smartfon("OnePlus", "9 Pro", 2021, 4500, 4999)

    # Wywoływanie metod na obiektach smartfonów
    iphone.uruchom_aplikacje("Instagram")
    galaxy.pobierz_plik("http://example.com/plik.pdf")
    oneplus.sprawdz_pojemnosc_baterii()
    iphone.podaj_rok_produkcji()
    galaxy.czy_wartosc(3500)


def zadanie4():
    class Student:
        def __init__(self, imie, nazwisko, wiek, kierunek, numer_indeksu):
            self.imie = imie
            self.nazwisko = nazwisko
            self.wiek = wiek
            self.kierunek = kierunek
            self.numer_indeksu = numer_indeksu

        def przedstaw_sie(self):
            print(
                f"Nazywam się {self.imie} {self.nazwisko}, mam {self.wiek} lat i studiuję na kierunku {self.kierunek}.\n")

        def zmien_kierunek(self, nowy_kierunek):
            self.kierunek = nowy_kierunek
            print(f"{self.imie} zmienił kierunek na {self.kierunek}.\n")

        def ustaw_numer_indeksu(self, nowy_numer_indeksu):
            self.numer_indeksu = nowy_numer_indeksu
            print(f"{self.imie} zmienił numer indeksu na {self.numer_indeksu}.\n")

        def dodaj_przedmiot(self, nazwa_przedmiotu):
            print(f"{self.imie} dodał przedmiot {nazwa_przedmiotu} do swojego planu zajęć.\n")

        def sprawdz_oceny(self):
            print(f"{self.imie} sprawdza swoje oceny z aktualnego semestru.\n")

    # Tworzenie obiektów studentów
    student1 = Student("Jan", "Kowalski", 21, "Informatyka", "123456")
    student2 = Student("Anna", "Nowak", 20, "Psychologia", "789012")
    student3 = Student("Adam", "Wójcik", 22, "Prawo", "345678")

    # Wywoływanie metod na obiektach studentów
    student1.przedstaw_sie()
    student2.zmien_kierunek("Socjologia")
    student3.ustaw_numer_indeksu("567890")
    student1.dodaj_przedmiot("Algorytmy i struktury danych")
    student2.sprawdz_oceny()


while True:
    print("\n\nLABORATORIUM 13 - PATRYCJA BRODZIK")
    print("1 - Zadanie 1")
    print("2 - Zadanie 2")
    print("3 - Zadanie 3")
    print("4 - Zadanie 4")
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
        elif choose == 4:
            zadanie4()
        else:
            print("Nieprawidłowy wybór. Wybierz opcję od 0 do 4.")
    except ValueError:
        print("Nieprawidłowy wybór. Wybierz opcję od 0 do 4.")

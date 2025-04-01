#   Patrycja Brodzik   dsw50708@student.dsw.edu.pl

def zadanie1():
    class Restaurant:
        def __init__(self, name):
            self.name = name

        def display_menu(self):
            pass

    class IceCreamStand(Restaurant):
        def __init__(self, name):
            super().__init__(name)
            self.flavors = []

        def display_menu(self):
            print("Available ice cream flavors:")
            for flavor in self.flavors:
                print(flavor)

        def add_flavor(self, flavor):
            self.flavors.append(flavor)

    class CoffeeShop(Restaurant):
        def __init__(self, name):
            super().__init__(name)
            self.coffee = []

        def display_menu(self):
            print("Available coffees:")
            for coffee in self.coffee:
                print(coffee)

        def add_coffee(self, coffee):
            self.coffee.append(coffee)

    ice_cream_stand = IceCreamStand("Ice Cream Stand")
    ice_cream_stand.add_flavor("Vanilla")
    ice_cream_stand.add_flavor("Chocolate")
    ice_cream_stand.add_flavor("Strawberry")

    coffee_shop = CoffeeShop("Coffee Shop")
    coffee_shop.add_coffee("Americano")
    coffee_shop.add_coffee("Latte")

    ice_cream_stand.display_menu()
    coffee_shop.display_menu()

    # Abstrakcja: Klasy IceCreamStand i CoffeeShop są konkretnymi implementacjami abstrakcyjnej klasy
    # Restaurant.Dzięki temu możemy definiować ogólną strukturę restauracji i jej zachowania,
    # jednocześnie pozwalając na specjalizację tych klas poprzez dodanie własnych atrybutów i metod.

    # Dziedziczenie: Klasy IceCreamStand i CoffeeShop dziedziczą po klasie Restaurant, co oznacza, że
    # odziedziczą jej właściwości i metody. Dzięki temu można uniknąć duplikacji kodu i wykorzystać
    # wspólne cechy restauracji.

    # Enkapsulacja: Atrybuty flavors i coffee w klasach IceCreamStand i CoffeeShop są przechowywane
    # jako prywatne (nie mają dostępu z zewnątrz), dzięki czemu są chronione przed bezpośrednią
    # manipulacją. Możemy zdefiniować odpowiednie metody (add_flavor, add_coffee) do zarządzania
    # tymi atrybutami, aby utrzymać kontrolę nad nimi.

    # Polimorfizm: Metody display_menu w klasach IceCreamStand i CoffeeShop mają taką samą nazwę i
    # podobny interfejs, ale zachowują się inaczej w zależności od implementacji w danej klasie. Dzięki
    # temu możemy używać tych metod w sposób jednolity, niezależnie od konkretnego typu obiektu, co
    # ułatwia rozszerzanie programu i jego elastyczność.

def zadanie2():
    class Beer:
        def __init__(self, name, category, alcohol_percentage, price):
            self.name = name
            self.category = category
            self.alcohol_percentage = alcohol_percentage
            self.price = price
            self.reviews = []

        def add_review(self, review):
            self.reviews.append(review)

        def get_average_rating(self):
            if not self.reviews:
                return 0
            total_rating = sum(review.rating for review in self.reviews)
            return total_rating / len(self.reviews)

        def __str__(self):
            return f"Beer: {self.name}, Category: {self.category}, Alcohol: {self.alcohol_percentage}%, Price: {self.price}"

    class Review:
        def __init__(self, comment, rating):
            self.comment = comment
            self.rating = rating

    class Sklep:
        def __init__(self):
            self.beers = []

        def add_beer(self, beer):
            self.beers.append(beer)

        def sort_by_rating(self):
            self.beers.sort(key=lambda beer: beer.get_average_rating(), reverse=True)

        def sort_by_name(self):
            self.beers.sort(key=lambda beer: beer.name)

        def display_beers(self):
            for beer in self.beers:
                print(beer)

    # Tworzenie obiektów Beer
    beer1 = Beer("IPA", "Ale", 6.5, 15.99)
    beer2 = Beer("Stout", "Porter", 7.2, 12.99)
    beer3 = Beer("Pilsner", "Lager", 4.8, 10.99)

    # Dodawanie opinii
    beer1.add_review(Review("Great beer!", 4.5))
    beer1.add_review(Review("Could be better.", 3.2))
    beer2.add_review(Review("Amazing stout!", 4.8))
    beer3.add_review(Review("Refreshing pilsner.", 4.0))

    # Tworzenie obiektu Sklep
    shop = Sklep()

    # Dodawanie piw do sklepu
    shop.add_beer(beer1)
    shop.add_beer(beer2)
    shop.add_beer(beer3)

    # Sortowanie i wyświetlanie piw według ocen
    print("Sortowanie i wyświetlanie piw według ocen: ")
    shop.sort_by_rating()
    shop.display_beers()

    # Sortowanie i wyświetlanie piw według nazw
    print("\nSortowanie i wyświetlanie piw według nazw: ")
    shop.sort_by_name()
    shop.display_beers()

def zadanie3():
    class Obywatel:
        def __init__(self):
            self.imie = ""
            self.nazwisko = ""
            self.ulica = ""
            self.nr_domu = ""
            self.kod_pocztowy = ""
            self.miejscowosc = ""

        def wczytaj_dane(self):
            self.imie = input("Podaj imię: ")
            self.nazwisko = input("Podaj nazwisko: ")
            self.ulica = input("Podaj ulicę: ")
            self.nr_domu = input("Podaj numer domu: ")
            self.kod_pocztowy = input("Podaj kod pocztowy: ")
            self.miejscowosc = input("Podaj miejscowość: ")

        def wyswietl_wizytowke(self):
            print("----------------------")
            print(f"{self.imie} {self.nazwisko}")
            print(f"{self.ulica} {self.nr_domu}")
            print(f"{self.kod_pocztowy} {self.miejscowosc}")
            print("----------------------")

        def zapisz_do_pliku(self, nazwa_pliku):
            with open(nazwa_pliku, "w") as file:
                file.write("----------------------\n")
                file.write(f"{self.imie} {self.nazwisko}\n")
                file.write(f"{self.ulica} {self.nr_domu}\n")
                file.write(f"{self.kod_pocztowy} {self.miejscowosc}\n")
                file.write("----------------------\n")

    obywatel = Obywatel()

    obywatel.wczytaj_dane()

    obywatel.wyswietl_wizytowke()

    obywatel.zapisz_do_pliku("wizytowka.txt")

def zadanie4():
    class Card:
        def __init__(self, rank, suit):
            self.rank = rank
            self.suit = suit

        def __str__(self):
            return f"{self.rank} of {self.suit}"

    class Deck:
        def __init__(self):
            self.cards = []
            ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
            suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
            for suit in suits:
                for rank in ranks:
                    self.cards.append(Card(rank, suit))

        def display_deck(self):
            for card in self.cards:
                print(card)

        def compare_cards(self, card1, card2):
            if self.cards.index(card1) < self.cards.index(card2):
                print("Comparison result: the first card is smaller than the second")
            elif self.cards.index(card1) > self.cards.index(card2):
                print("Comparison result: the first card is larger than the second")
            else:
                print("Comparison result: both cards are the same")

        def sort_cards(self):
            self.cards.sort(key=lambda card: (card.rank, card.suit))

        def add_card(self, card):
            self.cards.append(card)

        def remove_card(self, card):
            self.cards.remove(card)

        def move_card(self, card, new_deck):
            if card in self.cards:
                self.remove_card(card)
                new_deck.add_card(card)

    # Tworzenie talii kart
    deck = Deck()

    # Wyświetlanie talii
    print("*** DECK DISPLAY ***")
    print('\x1b[38;2;255;0;0m' + f"-----------DECK DISPLAY-----------" + '\x1b[0m')
    deck.display_deck()
    print('\x1b[38;2;255;0;0m' + f"----------------------------------\n" + '\x1b[0m')

    # Porównywanie kart
    print('\x1b[38;2;255;0;0m' + f"-----------DECK COMPARE-----------" + '\x1b[0m')
    card1 = deck.cards[0]
    card2 = deck.cards[15]
    deck.compare_cards(card1, card2)
    print('\x1b[38;2;255;0;0m' + f"----------------------------------\n" + '\x1b[0m')

    # Sortowanie kart
    print('\x1b[38;2;255;0;0m' + f"------------DECK  SORT------------" + '\x1b[0m')
    deck.sort_cards()
    print("Sorted deck:")
    deck.display_deck()
    print('\x1b[38;2;255;0;0m' + f"----------------------------------\n" + '\x1b[0m')

    # Dodawanie karty
    print('\x1b[38;2;255;0;0m' + f"-------------DECK ADD-------------" + '\x1b[0m')
    new_card = Card("Ace", "Spades")
    deck.add_card(new_card)
    print("Deck after adding a card:")
    deck.display_deck()
    print('\x1b[38;2;255;0;0m' + f"----------------------------------\n" + '\x1b[0m')

    # Usuwanie karty
    print('\x1b[38;2;255;0;0m' + f"-----------DECK  REMOVE-----------" + '\x1b[0m')
    card_to_remove = deck.cards[5]
    deck.remove_card(card_to_remove)
    print("Deck after removing a card:")
    deck.display_deck()
    print('\x1b[38;2;255;0;0m' + f"----------------------------------\n" + '\x1b[0m')

    # Tworzenie drugiej talii kart
    new_deck = Deck()

    # Przenoszenie karty
    print('\x1b[38;2;255;0;0m' + f"------------DECK  MOVE------------" + '\x1b[0m')
    card_to_move = deck.cards[15]
    deck.move_card(card_to_move, new_deck)
    print("Deck after moving a card:")
    deck.display_deck()
    print("New deck:")
    new_deck.display_deck()
    print('\x1b[38;2;255;0;0m' + f"----------------------------------\n" + '\x1b[0m')

def zadanie5():
    class NumerPokoju:
        def __init__(self, pietro, pokoj):
            self.pietro = pietro
            self.pokoj = pokoj
            self.osoba = None

    class Osoba:
        def __init__(self, imie, nazwisko):
            self.imie = imie
            self.nazwisko = nazwisko

    class Hotel:
        def __init__(self, liczba_pieter, pokoje_na_pietro):
            self.liczba_pieter = liczba_pieter
            self.pokoje_na_pietro = pokoje_na_pietro
            self.pokoje = []
            self.wynajete_pokoje = []

            # Inicjalizacja listy pokoi
            for pietro in range(1, liczba_pieter + 1):
                for pokoj in range(1, pokoje_na_pietro + 1):
                    self.pokoje.append(NumerPokoju(pietro, pokoj))

        def czy_jest_wolny_pokoj(self):
            return len(self.pokoje) > len(self.wynajete_pokoje)

        def ile_jest_wolnych_pokoi(self):
            return len(self.pokoje) - len(self.wynajete_pokoje)

        def wynajmij_wolny_pokoj(self, osoba):
            if self.czy_jest_wolny_pokoj():
                wolny_pokoj = self.pokoje[0]
                wolny_pokoj.osoba = osoba
                self.wynajete_pokoje.append(wolny_pokoj)
                self.pokoje.remove(wolny_pokoj)
                return wolny_pokoj
            else:
                return None

        def czy_mozna_wynajac_sasiednie_pokoje(self, osoba):
            for i in range(len(self.pokoje) - 1):
                if (
                        self.pokoje[i].pietro == self.pokoje[i + 1].pietro
                        and self.pokoje[i].pokoj == self.pokoje[i + 1].pokoj - 1
                ):
                    return self.pokoje[i].pokoj
            return None

        def czy_osoba_wynajmuje_pokoj(self, nazwisko):
            for wynajety_pokoj in self.wynajete_pokoje:
                if wynajety_pokoj.osoba.nazwisko == nazwisko:
                    return True
            return False

        def pokoj_wynajmowany_przez_osobe(self, nazwisko):
            wynajete_pokoje_osoby = []
            for wynajety_pokoj in self.wynajete_pokoje:
                if wynajety_pokoj.osoba.nazwisko == nazwisko:
                    wynajete_pokoje_osoby.append(wynajety_pokoj)
            return wynajete_pokoje_osoby

        def zwolnij_pokoj(self, numer_pokoju):
            numer_pokoju.osoba = None
            self.pokoje.append(numer_pokoju)
            self.wynajete_pokoje.remove(numer_pokoju)

    hotel = Hotel(5, 10)

    print('\x1b[38;2;255;0;0m' + f"\n----------------------------------" + '\x1b[0m')
    print("Czy jest jakiś wolny pokój?", hotel.czy_jest_wolny_pokoj())
    print("Ile jest wolnych pokoi?", hotel.ile_jest_wolnych_pokoi())

    osoba1 = Osoba("Jan", "Kowalski")
    wynajety_pokoj = hotel.wynajmij_wolny_pokoj(osoba1)
    if wynajety_pokoj:
        print(f"Wynajęto pokój {wynajety_pokoj.pietro}-{wynajety_pokoj.pokoj}")
    print('\x1b[38;2;255;0;0m' + f"----------------------------------" + '\x1b[0m')

    print("Czy jest jakiś wolny pokój?", hotel.czy_jest_wolny_pokoj())
    print("Ile jest wolnych pokoi?", hotel.ile_jest_wolnych_pokoi())

    osoba2 = Osoba("Anna", "Nowak")
    wynajety_pokoj2 = hotel.wynajmij_wolny_pokoj(osoba2)
    if wynajety_pokoj2:
        print(f"Wynajęto pokój {wynajety_pokoj2.pietro}-{wynajety_pokoj2.pokoj}")
    print('\x1b[38;2;255;0;0m' + f"----------------------------------" + '\x1b[0m')

    print("Czy jest jakiś wolny pokój?", hotel.czy_jest_wolny_pokoj())
    print("Ile jest wolnych pokoi?", hotel.ile_jest_wolnych_pokoi())

    sasiednie_pokoje = hotel.czy_mozna_wynajac_sasiednie_pokoje(osoba2)
    if sasiednie_pokoje:
        print("Można wynająć sąsiednie pokoje, pierwszy pokój:", sasiednie_pokoje)
    else:
        print("Nie można wynająć sąsiednich pokoi")
    print('\x1b[38;2;255;0;0m' + f"----------------------------------" + '\x1b[0m')

    print("Czy osoba o nazwisku 'Nowak' wynajmuje jakiś pokój?", hotel.czy_osoba_wynajmuje_pokoj("Nowak"))

    wynajete_pokoje_osoby2 = hotel.pokoj_wynajmowany_przez_osobe("Nowak")
    if wynajete_pokoje_osoby2:
        print(f"Wynajęte pokoje przez osobę o nazwisku 'Nowak':")
        for wynajety_pokoj in wynajete_pokoje_osoby2:
            print(f"{wynajety_pokoj.pietro}-{wynajety_pokoj.pokoj}")

    hotel.zwolnij_pokoj(wynajety_pokoj2)
    print('\x1b[38;2;255;0;0m' + f"----------------------------------" + '\x1b[0m')

    print("Czy jest jakiś wolny pokój?", hotel.czy_jest_wolny_pokoj())
    print("Ile jest wolnych pokoi?", hotel.ile_jest_wolnych_pokoi())


while True:
    print("\n\nLABORATORIUM 15 - PATRYCJA BRODZIK")
    print("1 - Zadanie 1")
    print("2 - Zadanie 2")
    print("3 - Zadanie 3")
    print("3 - Zadanie 4")
    print("3 - Zadanie 5")
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
        elif choose == 5:
            zadanie5()
        else:
            print("Nieprawidłowy wybór. Wybierz opcję od 0 do 5.")
    except ValueError:
        print("Nieprawidłowy wybór. Wybierz opcję od 0 do 5.")
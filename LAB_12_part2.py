#   Patrycja Brodzik   dsw50708@student.dsw.edu.pl

def kalkulator_plac():
    print("\n*** ZADANIE 1 ***")

    def calculate_salary(gross_salary, tax_rate=0.17, health_insurance_rate=0.09, pension_insurance_rate=0.0976,
                         disability_insurance_rate=0.015, sickness_insurance_rate=0.0245, tax_deduction=43.76):
        # Obliczanie składki na ubezpieczenie zdrowotne
        health_insurance = health_insurance_rate * gross_salary
        health_insurance_tax = 0.0775 * health_insurance

        # Obliczanie składki na ubezpieczenie społeczne
        pension_insurance = pension_insurance_rate * gross_salary
        disability_insurance = disability_insurance_rate * gross_salary
        sickness_insurance = sickness_insurance_rate * gross_salary

        # Obliczanie podatku dochodowego
        taxable_income = gross_salary - health_insurance - pension_insurance - disability_insurance - sickness_insurance - tax_deduction
        tax_base = taxable_income - 800
        if tax_base < 0:
            tax_base = 0
        tax = tax_rate * tax_base

        # Obliczanie wynagrodzenia netto i brutto
        net_salary = gross_salary - health_insurance - health_insurance_tax - pension_insurance - disability_insurance - sickness_insurance - tax
        gross_salary = gross_salary

        # Zwracanie wyników
        return (gross_salary, net_salary)

    # Kalkulator płacy netto na brutto
    def net_to_gross(net_salary):
        gross_salary = net_salary / (1 - 0.09 - 0.0775 - 0.015 - 0.0245 - 0.17)
        return round(gross_salary, 2)

    # Kalkulator płacy brutto na netto
    def gross_to_net(gross_salary):
        (gross_salary, net_salary) = calculate_salary(gross_salary)
        return round(net_salary, 2)


    while True:
        print("\nKALKULATOR PŁACY NETTO/BRUTTO W POLSCE")
        print("1. Oblicz płacę netto")
        print("2. Oblicz płacę brutto")
        print("0. Wyjście do menu głównego")

        try:
            wybor = int(input("Wybierz opcję: "))

            if wybor == 1:
                brutto = float(input("Podaj kwotę brutto: "))
                print(f"Twoja płaca netto wynosi: {round(gross_to_net(brutto), 2)} zł")
            elif wybor == 2:
                netto = float(input("Podaj kwotę netto: "))
                print(f"Twoja płaca brutto wynosi: {round(net_to_gross(netto), 2)} zł")
            elif wybor == 0:
                break

            else:
                print("Nieprawidłowy wybór. Wybierz opcję od 0 do 2.")

        except ValueError:
            print("Nieprawidłowy wybór. Wybierz opcję od 0 do 2.")


def kalkulator_kosztow_pracodawcy():
    print("\n*** ZADANIE 2 ***")

    while True:
        print("\nKALKULATOR KOSZTÓW PRACODAWCY")
        print("1. Oblicz koszty brutto")
        print("2. Oblicz koszty netto")
        print("0. Wyjście do menu głównego")

        try:
            wybor = int(input("Wybierz opcję: "))

            if wybor == 1:
                netto = float(input("Podaj kwotę netto: "))
                brutto = netto / (1 - 0.0976 - 0.015 - 0.0245 - 0.09 - 0.0245 - 0.001)
                emerytalne = brutto * 0.0976
                rentowe = brutto * 0.015
                wypadkowe = brutto * 0.0245
                fundusz_pracy = brutto * 0.0245
                FGSP = brutto * 0.001
                koszty_brutto = brutto + emerytalne + rentowe + wypadkowe + fundusz_pracy + FGSP
                print(f"Koszty brutto dla kwoty netto {netto} zł wynoszą: {round(koszty_brutto, 2)} zł")
            elif wybor == 2:
                brutto = float(input("Podaj kwotę brutto: "))
                netto = brutto - (brutto * 0.0976) - (brutto * 0.015) - (brutto * 0.0245) - (brutto * 0.09) - (
                            brutto * 0.0245) - (brutto * 0.001)
                print(f"Koszty netto dla kwoty brutto {brutto} zł wynoszą: {round(netto, 2)} zł")
            elif wybor == 0:
                break
            else:
                print("Nieprawidłowy wybór. Wybierz opcję od 0 do 2.")
        except ValueError:
            print("Nieprawidłowy wybór. Wybierz opcję od 0 do 2.")


def test_informatyczny():
    print("\n*** ZADANIE 3 ***")

    pytania = [
        ["Co oznacza skrót HTML?", "a", {"a": "Hyper Text Markup Language", "b": "Hyperlinks and Text Markup Language",
                                         "c": "Home Tool Markup Language"}],
        ["Jak nazywa się język programowania stworzony przez Guido van Rossum?", "c",
         {"a": "Ruby", "b": "Perl", "c": "Python"}],
        ["Co to jest SQL?", "b", {"a": "Język programowania", "b": "Język zapytań do baz danych", "c": "Framework"}],
        ["Co oznacza skrót CSS?", "c",
         {"a": "Computer Style Sheets", "b": "Cascading Script Sheets", "c": "Cascading Style Sheets"}],
        ["Co to jest JavaScript?", "a", {"a": "Język programowania", "b": "Framework", "c": "System operacyjny"}],
        ["Co oznacza skrót PHP?", "a",
         {"a": "PHP Hypertext Preprocessor", "b": "Personal Home Page", "c": "Procedural Hypertext Processor"}],
        ["Jak nazywa się system kontroli wersji stworzony przez Linusa Torvaldsa?", "c",
         {"a": "GitLab", "b": "Bitbucket", "c": "Git"}],
        ["Co oznacza skrót IDE?", "b",
         {"a": "Integrated Document Environment", "b": "Integrated Development Environment",
          "c": "Integrated Database Environment"}],
        ["Co to jest framework?", "c",
         {"a": "Język programowania", "b": "System operacyjny", "c": "Struktura programistyczna"}],
        ["Jak nazywa się baza danych stworzona przez firmę Oracle?", "a",
         {"a": "Oracle Database", "b": "MySQL", "c": "PostgreSQL"}],
    ]

    punkty = 0

    print("TEST INFORMATYCZNY")

    for i, pytanie in enumerate(pytania, 1):
        print(f"\nPytanie {i}: {pytanie[0]}")
        for k, v in pytanie[2].items():
            print(f"{k}. {v}")
        odpowiedz = input("Odpowiedź: ").lower()
        if odpowiedz == pytanie[1]:
            punkty += 1

    print("\nWYNIK:")
    procenty = punkty / len(pytania) * 100

    if procenty < 50:
        ocena = "niedostateczna"
    elif procenty < 60:
        ocena = "dostateczna"
    elif procenty < 70:
        ocena = "dobra"
    elif procenty < 80:
        ocena = "bardzo dobra"
    else:
        ocena = "celująca"

    print(f"Uzyskałeś {punkty} punktów na {len(pytania)} możliwych, czyli {procenty}% poprawnych odpowiedzi.")
    print(f"Twoja ocena to: {ocena}.")


def convert_to_binary_units():
    print("\n*** ZADANIE 4 ***")

    def convert(size_in_metric_units, unit):
        units = {'B': 0, 'KB': 1, 'MB': 2, 'GB': 3, 'TB': 4, 'PB': 5}
        binary_size = size_in_metric_units * (1000 ** units[unit]) / (1024 ** units[unit])
        return binary_size

    print("*** Dlaczego producenci nas oszukują? ***")
    print("Producentom dysków twardych zależy na maksymalizacji swojego zysku, dlatego określenie pojemności dysku w jednostkach metrycznych (np. gigabajtach)\n"
          "pozwala na wyświetlenie większej liczby jednostek i wrażenie większej pojemności. Jednak w rzeczywistości, pojemność ta jest mniejsza, gdyż producenci stosują system dziesiętny,\n"
          "który opiera się na mnożniku 1000, zamiast binarnym, który opiera się na mnożniku 1024. Dlatego rzeczywista pojemność dysku będzie zawsze mniejsza niż ta wyświetlana na opakowaniu.\n")

    print("Konwersja jednostek pojemności dysków twardych")
    print("----------------------------------------------")
    size = float(input("Podaj pojemność dysku w jednostkach metrycznych: "))
    unit = input("Podaj jednostkę metryczną (B, KB, MB, GB, TB, PB): ")
    binary_size = convert(size, unit)
    print(f"Rzeczywista pojemność dysku w jednostkach binarnych: {binary_size:.2f} B")


def convert_currencies():
    print("\n*** ZADANIE 5 ***")
    def thb_usd_converter():

        def thb_to_usd(thb):
            """Przelicza THB na USD"""
            return thb / 31.2

        def usd_to_thb(usd):
            """Przelicza USD na THB"""
            return usd * 31.2

        """Funkcja obsługująca przeliczanie walut THB-USD"""
        print("\n1. THB -> USD")
        print("2. USD -> THB")
        option = input("Wybierz opcję: ")

        if option == "1":
            thb = float(input("Podaj wartość THB: "))
            usd = thb_to_usd(thb)
            print("{0} THB to {1:.2f} USD".format(thb, usd))
        elif option == "2":
            usd = float(input("Podaj wartość USD: "))
            thb = usd_to_thb(usd)
            print("{0} USD to {1:.2f} THB".format(usd, thb))
        else:
            print("Niepoprawna opcja")

    def btc_usd_converter():

        def btc_to_usd(btc):
            """Przelicza BTC na USD"""
            return btc * 50000

        def usd_to_btc(usd):
            """Przelicza USD na BTC"""
            return usd / 50000

        """Funkcja obsługująca przeliczanie walut BTC-USD"""
        print("\n1. BTC -> USD")
        print("2. USD -> BTC")
        option = input("Wybierz opcję: ")

        if option == "1":
            btc = float(input("Podaj wartość BTC: "))
            usd = btc_to_usd(btc)
            print("{0} BTC to {1:.2f} USD".format(btc, usd))
        elif option == "2":
            usd = float(input("Podaj wartość USD: "))
            btc = usd_to_btc(usd)
            print("{0} USD to {1:.6f} BTC".format(usd, btc))
        else:
            print("Niepoprawna opcja")

    def btn_usd_converter():

        def btn_to_usd(btn):
            """Przelicza BTN na USD"""
            return btn * 0.014

        def usd_to_btn(usd):
            """Przelicza USD na BTN"""
            return usd / 0.014

        """Funkcja obsługująca przeliczanie walut BTN-USD"""
        print("\n1. BTN -> USD")
        print("2. USD -> BTN")
        option = input("Wybierz opcję: ")

        if option == "1":
            btn = float(input("Podaj wartość BTN: "))
            usd = btn_to_usd(btn)
            print("{0} BTN to {1:.2f} USD".format(btn, usd))
        elif option == "2":
            usd = float(input("Podaj wartość USD: "))
            btn = usd_to_btn(usd)
            print("{0} USD to {1:.6f} BTC".format(usd, btn))
        else:
            print("Niepoprawna opcja")

    def mro_usd_converter():

        def mro_to_usd(mro):
            """Przelicza MRO na USD"""
            return mro * 0.027

        def usd_to_mro(usd):
            """Przelicza USD na MRO"""
            return usd / 0.027

        """Funkcja obsługująca przeliczanie walut MRO-USD"""
        print("\n1. MRO -> USD")
        print("2. USD -> MRO")
        option = input("Wybierz opcję: ")

        if option == "1":
            mro = float(input("Podaj wartość MRO: "))
            usd = mro_to_usd(mro)
            print("{0} BTN to {1:.2f} USD".format(mro, usd))
        elif option == "2":
            usd = float(input("Podaj wartość USD: "))
            mro = usd_to_mro(usd)
            print("{0} USD to {1:.6f} BTC".format(usd, mro))
        else:
            print("Niepoprawna opcja")

    def eth_usd_converter():

        def eth_to_usd(eth):
            """Przelicza ETH na USD"""
            return eth * 1800

        def usd_to_eth(usd):
            """Przelicza USD na ETH"""
            return usd / 1800

        """Funkcja obsługująca przeliczanie walut ETH-USD"""
        print("\n1. ETH -> USD")
        print("2. USD -> ETH")
        option = input("Wybierz opcję: ")

        if option == "1":
            eth = float(input("Podaj wartość ETH: "))
            usd = eth_to_usd(eth)
            print("{0} BTN to {1:.2f} USD".format(eth, usd))
        elif option == "2":
            usd = float(input("Podaj wartość USD: "))
            eth = usd_to_eth(usd)
            print("{0} USD to {1:.6f} BTC".format(usd, eth))
        else:
            print("Niepoprawna opcja")

    while True:
        print("\nWybierz walutę do przeliczenia:")
        print("1. Baht Tajski (THB) - Dolary amerykańskie (USD)")
        print("2. Bitcoin (BTC) - Dolary amerykański(USD)")
        print("3. Ngultrum bhutański(BTN) - Dolaryamerykańskie(USD)")
        print("4. Ugija mauretańska(MRO) - Dolary amerykańskie (USD)")
        print("5. Ethereum(ETH) – Dolary amerykańskie (USD)")
        print("0. Wyjście do menu głównego")

        try:
            option = input("Wybierz opcję: ")

            if option == "0":
                break
            if option == "1":
                thb_usd_converter()
            elif option == "2":
                btc_usd_converter()
            elif option == "3":
                btn_usd_converter()
            elif option == "4":
                mro_usd_converter()
            elif option == "5":
                eth_usd_converter()
            else:
                print("Nieprawidłowy wybór. Wybierz opcję od 0 do 5.")
        except ValueError:
            print("Nieprawidłowy wybór. Wybierz opcję od 0 do 5.")


def temperature_converter():
    print("\n*** ZADANIE 6 ***")

    def celsius_to_fahrenheit(celsius):
        fahrenheit = (celsius * 9 / 5) + 32
        return fahrenheit

    def fahrenheit_to_celsius(fahrenheit):
        celsius = (fahrenheit - 32) * 5 / 9
        return celsius

    def kelvin_to_fahrenheit(kelvin):
        fahrenheit = (kelvin - 273.15) * 9 / 5 + 32
        return fahrenheit

    def fahrenheit_to_kelvin(fahrenheit):
        kelvin = (fahrenheit - 32) * 5 / 9 + 273.15
        return kelvin

    def kelvin_to_celsius(kelvin):
        celsius = kelvin - 273.15
        return celsius

    def celsius_to_kelvin(celsius):
        kelvin = celsius + 273.15
        return kelvin

    while True:
        print("\n1. Przelicz temperaturę z Celsjusza na Fahrenheita")
        print("2. Przelicz temperaturę z Fahrenheita na Celsjusza")
        print("3. Przelicz temperaturę z Kelvina na Fahrenheita")
        print("4. Przelicz temperaturę z Fahrenheita na Kelvina")
        print("5. Przelicz temperaturę z Kelvina na Celsjusza")
        print("6. Przelicz temperaturę z Celsjusza na Kelvina")
        print("0. Wyjście do menu głównego")
        try:
            wybor = int(input("Wybierz opcję: "))

            if wybor == 0:
                break
            elif wybor == 1:
                celsius = float(input("Podaj temperaturę w stopniach Celsjusza: "))
                fahrenheit = celsius_to_fahrenheit(celsius)
                print("Temperatura w stopniach Fahrenheita: {:.2f}".format(fahrenheit))
                if celsius <= 0:
                    print("Woda zamarza")
                elif celsius >= 100:
                    print("Woda wrze")
            elif wybor == 2:
                fahrenheit = float(input("Podaj temperaturę w stopniach Fahrenheita: "))
                celsius = fahrenheit_to_celsius(fahrenheit)
                print("Temperatura w stopniach Celsjusza: {:.2f}".format(celsius))
                if fahrenheit <= 32:
                    print("Woda zamarza")
                elif fahrenheit >= 212:
                    print("Woda wrze")
            elif wybor == 3:
                kelvin = float(input("Podaj temperaturę w stopniach Kelvina: "))
                fahrenheit = kelvin_to_fahrenheit(kelvin)
                print("Temperatura w stopniach Fahrenheita: {:.2f}".format(fahrenheit))
                if kelvin <= 273.15:
                    print("Woda zamarza")
                elif kelvin >= 373.15:
                    print("Woda wrze")
            elif wybor == 4:
                fahrenheit = float(input("Podaj temperaturę w stopniach Fahrenheita: "))
                kelvin = fahrenheit_to_kelvin(fahrenheit)
                print("Temperatura w stopniach Kelvina: {:.2f}".format(kelvin))
                if fahrenheit <= 32:
                    print("Woda zamarza")
                elif fahrenheit >= 212:
                    print("Woda wrze")
            elif wybor == 5:
                kelvin = float(input("Podaj temperaturę w stopniach Kalvina: "))
                celsius = kelvin_to_celsius(kelvin)
                print("Temperatura w stopniach Celsjusza: {:.2f}".format(celsius))
                if kelvin <= 273.15:
                    print("Woda zamarza")
                elif kelvin >= 373.15:
                    print("Woda wrze")
            elif wybor == 6:
                celsius = float(input("Podaj temperaturę w stopniach Celsjusza: "))
                kelvin = celsius_to_kelvin(celsius)
                print("Temperatura w stopniach Kelvina: {:.2f}".format(kelvin))
                if celsius <= 0:
                    print("Woda zamarza")
                elif celsius >= 100:
                    print("Woda wrze")
            else:
                print("Nieprawidłowy wybór. Wybierz opcję od 0 do 6.")
        except ValueError:
            print("Nieprawidłowy wybór. Wybierz opcję od 0 do 6.")


def D_M_R():
    print("\n*** ZADANIE 7 ***")
    import datetime

    def yesterday(today):
        """Funkcja zwraca datę wczorajszą."""
        yesterday = today - datetime.timedelta(days=1)
        return yesterday.strftime('%d.%m.%Y')

    def tomorrow(today):
        """Funkcja zwraca datę jutrzejszą."""
        tomorrow = today + datetime.timedelta(days=1)
        return tomorrow.strftime('%d.%m.%Y')

    def is_leap_year(year):
        """Funkcja sprawdza, czy podany rok jest przestępny."""
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def easter_date(year):
        """Funkcja zwraca datę Wielkanocy dla danego roku."""
        a = year % 19
        b, c = divmod(year, 100)
        d, e = divmod(b, 4)
        f = (b + 8) // 25
        g = (b - f + 1) // 3
        h = (19 * a + b - d - g + 15) % 30
        i, k = divmod(c, 4)
        l = (32 + 2 * e + 2 * i - h - k) % 7
        m = (a + 11 * h + 22 * l) // 451
        month = (h + l - 7 * m + 114) // 31
        day = (h + l - 7 * m + 114) % 31 + 1
        return datetime.date(year, month, day).strftime('%d.%m.%Y')

    def birth_day_of_week(date):
        """Funkcja zwraca dzień tygodnia, w którym urodził się użytkownik."""
        birth_date = datetime.datetime.strptime(date, '%d.%m.%Y').date()
        days = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela']
        return days[birth_date.weekday()]

    while True:
        print("\n1. Wyświetl dzisiejszą datę")
        print("2. Wyświetl wczorajsza datę")
        print("3. Wyświetl jutrzejszą datę")
        print("4. Sprawdź czy rok jest przestępny")
        print("5. Sprawdź datę wielkanocy")
        print("6. Sprawdź dzień tygodnia w którym sie urodziłeś")
        print("0. Wyjście do menu głównego")

        try:
            wybor = int(input("Wybierz opcję: "))
            today = datetime.date.today()

            if wybor == 0:
                break
            elif wybor == 1:
                print("Dzisiaj jest:", today.strftime('%d.%m.%Y'))
            elif wybor == 2:
                print("Wczoraj był:", yesterday(today))
            elif wybor == 3:
                print("Jutro będzie:", tomorrow(today))
            elif wybor ==4:
                year = int(input("Proszę podać rok: "))
                print("Czy rok jest przestępny:", is_leap_year(year))
            elif wybor == 5:
                year = int(input("Proszę podać rok: "))
                print(f"Data Wielkanocy w roku {year}:", easter_date(year))
            elif wybor == 6:
                birth_date = input("Proszę podać datę urodzin w formacie dd.mm.yyyy: ")
                print("Urodziłeś się w:", birth_day_of_week(birth_date))
            else:
                print("Nieprawidłowy wybór. Wybierz opcję od 0 do 6.")
        except ValueError:
            print("Nieprawidłowy wybór. Wybierz opcję od 0 do 6.")


while True:
    print("\n\nLABORATORIUM 12 part 2 - PATRYCJA BRODZIK")
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
            print("Goodybye!")
            break
        elif wybor == 1:
            kalkulator_plac()
        elif wybor == 2:
            kalkulator_kosztow_pracodawcy()
        elif wybor == 3:
            test_informatyczny()
        elif wybor == 4:
            convert_to_binary_units()
        elif wybor == 5:
            convert_currencies()
        elif wybor == 6:
            temperature_converter()
        elif wybor == 7:
            D_M_R()
        else:
            print("Nieprawidłowy wybór. Wybierz opcję od 0 do 7.")
    except ValueError:
        print("Nieprawidłowy wybór. Wybierz opcję od 0 do 7.")


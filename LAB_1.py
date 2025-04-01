#   Patrycja Brodzik   dsw50708@student.dsw.edu.pl

#Zadanie 1
print("Zadanie 1: Napisz program, który pobierze od użytkownika dwie liczby i zwróci ich sumę, różnicę, iloczyn oraz iloraz (jeżeli można policzyć).\n")

l_1 = float(input("Proszę podać pierwszą liczbę:   "))
l_2 = float(input("Proszę podać drugą liczbę:   "))

suma = l_1 + l_2
różnica = l_1 - l_2
iloczyn = l_1 * l_2

try:
    iloraz = l_1 / l_2
except ZeroDivisionError:
    iloraz = "NIE WOLNO DZIELIĆ PRZEZ 0"

print(f"\nSuma:   {suma}\n"
      f"Różnica:   {różnica}\n"
      f"Iloczyn:   {iloczyn}\n"
      f"Iloraz:   {iloraz}")


#Zadanie 2
print("\n\nZadanie 2: Wykonaj dzielenie modulo dla liczb 1, 69, 666, 10000 i największej liczby jaką znasz.\nDla jakiej najmniejszej i największej liczby typu int i float jesteś w stanie wykonać dzielenie modulo?\n")

dzielnik = int(input("Proszę podać dzielnik:   "))
l_int = int(input("Proszę podać największą liczbę typu int:   "))
l_float = float(input("Prosze podać największą liczbę typu float:   "))

print(f"\n1 mod {dzielnik} = {1 % dzielnik}\n"
      f"69 mod {dzielnik} = {69 % dzielnik}\n"
      f"666 mod {dzielnik} = {666 % dzielnik}\n"
      f"1000 mod {dzielnik} = {1000 % dzielnik}\n"
      f"{l_int} mod {dzielnik} = {l_int % dzielnik}\n"
      f"{l_float} mod {dzielnik} = {l_float % dzielnik}")

# Największą i najmniejszą liczbą ze względu na ograniczony zakres zmiennej typu int jest liczba +/- :
# 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
# 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
# 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
# 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
# 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999


#Zadanie 3
print(f"\n\nZadanie 3:  Napisz skrypt, za pomocą zadeklarowanych zmiennych, który obliczy ile czasu i kilometrów ma rok świetlny.\n")

C = 299792.458 #prędkość światła wyrażona w km/s
Year = 31556926 #Rok wyrażony w sekundach

print(f"Prędkość światła:   {C} km/s\n"
      f"Czas:   {Year} sekund\n"
      f"Odległość jednego roku świetlnego wynosi:   {C * Year} kilometrów")


#Zadanie 4
print(f"\n\nZadanie 4: Napisz skrypt, za pomocą zadeklarowanych zmiennych, który obliczy ile sekund ma godzina,\nile sekund ma doba, ile sekund ma rok, ile sekund ma twoje życie.")

from datetime import date, datetime

sekunda = 1
godzina = 3600
doba = 24
rok = 365

sekund_w_godzinie = sekunda * godzina
sekund_w_dobie = sekunda * godzina * doba
sekund_w_roku = sekunda * godzina * doba * rok

while True:
      try:
            data_urodzenia = input("Proszę podać datę urodzenia w formacie RRRR-MM-DD:   ").split('-')
            rok_u, miesiąc_u, dzień_u = [int(i) for i in data_urodzenia]
            rok_urodzenia = date(rok_u, miesiąc_u, dzień_u)
      except ValueError:
            print("Prosze podać poprawną datę!")
            continue
      break

while True:
      try:
            godzina_narodzin = input("Proszę podać godzinę narodzin w formacie GG:MM:SS:   ").split(':')
            godzina_u, minuta_u, sekunda_u = [int(i) for i in godzina_narodzin]
            rok_urodzenia = datetime(rok_u, miesiąc_u, dzień_u, godzina_u, minuta_u, sekunda_u)
      except ValueError:
            print("Proszę podać prawidłowy czas!")
      break

aktualna_data = datetime.now()
różnica_czasu = aktualna_data - rok_urodzenia

dni = różnica_czasu.days
sekundy_żyćka = różnica_czasu.seconds
sekundy_żyćka += dni * sekund_w_dobie

print(f"\nGodzina ma:   {str(sekund_w_godzinie)}   sekund,\n"
      f"doba ma:   {str(sekund_w_dobie)}   sekund,\n"
      f"rok ma:   {str(sekund_w_roku)}   sekund,\n"
      f"a twoje życie ma:   {str(sekundy_żyćka)}   sekund.")


#Zadanie 5
print(f"\n\nZadanie 5: Napisz skrypt pozwalający przeliczyć cale na centymetry (1 cal = 2.54 cm).\n")

cal = float(input("Proszę podać liczbę wyrażoną w calach:   "))

cm = cal * 2.54
print(f"{cal} cali to {round(cm, 3)}")


#Zadanie 6
print(f"\n\nZadanie 6: Oblicz średnią prędkość jazdy samochodu, który dystans 30km pokonał w 15 minut. Wynik podaj w km/h.\nO ile wynik się zmieni jeśli kolejne 30 km przejechał 12 minut? Z jaką średnią prędkością przejechał samochód cały dystans\n")

distance_1 = 30
time_1 = 15 / 60
speed_1 = 1 * distance_1 / time_1

distance_2 = 30
time_2 = 12 / 60
speed_2 = 1 * distance_2 / time_2

the_whole_distance = (speed_1 + speed_2) / 2
speed_difference = the_whole_distance - speed_1

print(f"Średnia prędkość samochodu, który poonał dystans 30 km w 15 minut:   {speed_1} km/h\n"
      f"Róźnica prędkości:   {speed_difference} km/h\n"
      f"Średnia prędkość samochodu na całym dystansie:   {the_whole_distance} km/h")
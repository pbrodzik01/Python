#   Patrycja Brodzik   dsw50708@student.dsw.edu.pl

import random

#Zadanie 1
print("Zadanie 1:\n")

menu = {
    "rosołek" : 12.50,
    "pierogi ruskie" : 23.40,
    "żeberka" : 42.80,
    "tatar" : 18.50,
    "piwo" : 10,
    "naleśniki z serem" : 16.90,
    "krokiety" : 28.40,
    "sernik wiedeński" : 34.80,
    "schabowy z pieczonymi ziemniorami" : 39.99,
}

print("*** MENU ***")
for klucz, wartość in menu.items():
    print(klucz, wartość)
print("***      ***\n")

del menu["piwo"]
del menu["żeberka"]

print("*** MENU ***")
for klucz, wartość in menu.items():
    print(klucz, wartość)
print("***      ***\n")

menu[f'{input("Proszę podać nazwę:   ")}'] = f'{input("Proszę podać wartość:   ")}'






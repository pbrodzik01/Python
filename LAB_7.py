#   Patrycja Brodzik   dsw50708@student.dsw.edu.pl

import random

#Zadanie 1
print("\n\nZadanie 1: \n")

krotka1 = (666, "Freddy", "Pacan", 69, 1000, "Andżyj")

print(f"Krotka:   {krotka1}")
print(f"Długość:   {len(krotka1)}\n")
print(id(krotka1))

krotka1 += (5, "Popromszę trzy")
print(f"Krotka:   {krotka1}")
print(f"Długość:   {len(krotka1)}\n")
print(id(krotka1))

lista1 = list(krotka1)
print(f"Tablica:   {lista1}")


#Zadanie 2
print("\n\nZadanie 2:\n")

krotka2 = tuple(random.randint(0,10) for e in range(100))
print(f'***KROTKA***\n{krotka2}\n\n***ANALIZA***')

print(f"Liczba 0 wystąpiła:   {krotka2.count(0)}   razy.")
print(f"Liczba 1 wystąpiła:   {krotka2.count(1)}   razy.")
print(f"Liczba 1 wystąpiła:   {krotka2.count(2)}   razy.")

ele_parz = ""
print("\nElementy parzyste:")
for elem in krotka2:
    if elem % 2 == 0:
        ele_parz += f"{elem} "
print(ele_parz)

ele_nparz = ""
print("\nElementy nieparzyste:")
for elem in krotka2:
    if elem % 2 == 1:
        ele_nparz += f"{elem} "
print(ele_nparz)

krotka2 += (11, 12, 13)
print(f"\nPo dodaniu trzech elementów krotka t ma długość {len(krotka2)}")

#Zadanie 3
print("\n\nZadanie 3:\n")

A = tuple(range(0, 200, 2))[:100]
B = tuple(range(1, 200, 2))[:100]
C = A + B

print(f"Długość krotki C wynosi {len(C)}.")

print(f"Liczba 0 {'jest' if 0 in C else 'nie jest'} w krotce C.")
print(f"Liczba 100 {'jest' if 100 in C else 'nie jest'} w krotce C.")

idx_0 = C.index(0)
idx_100 = C.index(100)

print(f"Przed zamianą: indeks 0 to {idx_0}, a indeks 100 to {idx_100}.")

C = C[:idx_0] + (100,) + C[idx_0+1:idx_100] + (0,) + C[idx_100+1:]

print(f"Po zamianie: indeks 0 to {C.index(0)}, a indeks 100 to {C.index(100)}.")

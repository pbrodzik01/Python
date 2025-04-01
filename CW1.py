def analiza_tekst(path):
    plik = open(path, encoding='utf-8')
    tekst = (plik.read()).lower()
    znaki = [',','.','!',':','?','-','/']
    for i in tekst:
        if i in znaki:
            tekst = tekst.replace(i,"")
    tab = tekst.split()
    tab_wyrazów = list(set(tab))
    raport = []

    for i in range(len(tab_wyrazów)):
        raport.append((tab.count(tab_wyrazów[i]),tab_wyrazów[i]))
    raport.sort()
    raport.reverse()
    return raport


path = input("Proszę podać ścieżkę do pliku tekstu:   ")
print(f'\n*** ANALIZA TEKSTU ***')
for i in range(len(analiza_tekst(f'{path}'))):
    print(analiza_tekst(f'{path}')[i])
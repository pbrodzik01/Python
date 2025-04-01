plik = open('tekst.txt.', 'rt')
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

print(f'*** TEKST ***\n{tekst}\n\n*** ANALIZA TEKSTU ***')
for i in range(len(raport)):
    print(raport[i])
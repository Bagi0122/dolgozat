konyvtar=[]
with open("konyvtar.txt", 'r', encoding='utf-8') as forras, \
    open('konyvtar1.txt', 'w', encoding='utf-8') as cel:
    fejlec=forras.readline()
    for sor in forras:
        adat=sor.strip().split(',')
        konyv={'szerz': adat[0], 'cm':adat[1], 'kiads':adat[2], 'ISBN':adat[3], 'llapot':adat[4]}
        konyvtar.append(konyv)
        print(konyv,file=cel)
print(f'{konyvtar}')

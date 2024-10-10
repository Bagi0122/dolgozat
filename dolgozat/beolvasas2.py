#beolvasas2

halozat=[]
with open("hálózat.txt", 'r', encoding='utf-8') as forras, \
    open('hálózat1.txt', 'w', encoding='utf-8') as cel:
    fejlec=forras.readline()
    for sor in forras:
        adat=sor.strip().split(',')
        halozat={'PC': adat[0], 'PT':adat[1], 'R':adat[2], 'SWR':adat[3], 'Admin':adat[4], 'SWL':adat[5], 'server':adat[6]}
        halozat.append(halozat)
        print(halozat,file=cel)
print(f'{halozat}')

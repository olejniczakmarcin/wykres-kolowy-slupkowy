import matplotlib.pyplot as plt

liczba_miesiecy = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
wczytana_liczba_sprzedanych_aut_bmw=open('bmw2.txt',"r").readlines()
wczytana_liczba_sprzedanych_aut_opel=open('opel2.txt',"r").readlines()   
wczytana_liczba_sprzedanych_aut_ford=open('ford2.txt',"r").readlines()

liczba_sprzedanych_aut_bmw=[]
liczba_sprzedanych_aut_opel=[]
liczba_sprzedanych_aut_ford=[]

for i in wczytana_liczba_sprzedanych_aut_bmw:
    liczba_sprzedanych_aut_bmw=i.split(',') 
for i in range(12):
    liczba_sprzedanych_aut_bmw[i]=int(liczba_sprzedanych_aut_bmw[i])
for i in wczytana_liczba_sprzedanych_aut_opel:
    liczba_sprzedanych_aut_opel=i.split(',')
for i in range(12):
    liczba_sprzedanych_aut_opel[i]=int(liczba_sprzedanych_aut_opel[i])
for i in wczytana_liczba_sprzedanych_aut_ford:
    liczba_sprzedanych_aut_ford=i.split(',')
for i in range(12):
    liczba_sprzedanych_aut_ford[i]=int(liczba_sprzedanych_aut_ford[i])

nieposortowana_liczba_sprzedanych_aut_przez_producentow=[liczba_sprzedanych_aut_bmw[11],liczba_sprzedanych_aut_ford[11],liczba_sprzedanych_aut_opel[11]]
posortowana_rosnaco_liczba_sprzedanych_aut=sorted(nieposortowana_liczba_sprzedanych_aut_przez_producentow) 
posorotowane_rosnaco_listy_sprzedanych_aut=[list(),list(),list()]
posortowane_rosnaco_marki_sprzedanych_aut = [' ',' ',' ']
i=0

for l in posortowana_rosnaco_liczba_sprzedanych_aut:
    if(l==liczba_sprzedanych_aut_ford[11]):
        posortowane_rosnaco_marki_sprzedanych_aut[i]="FORD"
        posorotowane_rosnaco_listy_sprzedanych_aut[i]=liczba_sprzedanych_aut_ford
        i=i+1
    if(l==liczba_sprzedanych_aut_bmw[11]):
        posorotowane_rosnaco_listy_sprzedanych_aut[i]=liczba_sprzedanych_aut_bmw
        posortowane_rosnaco_marki_sprzedanych_aut[i]="BMW"
        i=i+1
    if(l==liczba_sprzedanych_aut_opel[11]):
        posorotowane_rosnaco_listy_sprzedanych_aut[i]=liczba_sprzedanych_aut_opel
        posortowane_rosnaco_marki_sprzedanych_aut[i]="OPEL"
        i=i+1

okno, osie = plt.subplots()
osie.tick_params(color='red',width=2,labelsize=12)
kolory=['blue','orange','green']
osie.annotate('$liczba$ $sprzedawanych$ $aut$ $w$ $roku$ $2018$', xy=(0, 1), xytext=(-55,-260), rotation=90, xycoords='axes fraction', textcoords='offset points', fontsize=14,color='red')
osie.annotate('$numer$ $miesiąca$', xy=(1, 0), xytext=(-250,-30), xycoords='axes fraction', textcoords='offset points', fontsize=15,color='blue')
osie.stackplot(liczba_miesiecy, posorotowane_rosnaco_listy_sprzedanych_aut, labels=posortowane_rosnaco_marki_sprzedanych_aut,colors=kolory,alpha=0.4)
osie.set_facecolor('silver')
osie.legend(loc='upper left')
plt.title('STACKPLOT CHART',x=0.5,y=1.07, fontsize=15,color='orange')
okno.patch.set_facecolor('xkcd:aqua')
plt.grid()
plt.show()

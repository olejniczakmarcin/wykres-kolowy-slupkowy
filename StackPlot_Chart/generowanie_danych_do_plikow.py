import os

if os.path.exists("bmw2.txt"):
    os.remove("bmw2.txt")
if os.path.exists("opel2.txt"):
    os.remove("opel2.txt")
if os.path.exists("ford2.txt"):
    os.remove("ford2.txt")

srednia_liczba_sprzedanych_aut_bmw_w_miesiac=207500
srednia_liczba_sprzedanych_aut_opel_w_miesiac=343806
srednia_liczba_sprzedanych_aut_ford_w_miesiac=477859
suma_sprzedanych_bmw=0
suma_sprzednaych_opli=0
suma_sprzedanych_fordow=0

with open("bmw2.txt","w+") as file:
    for i in range(12):
        suma_sprzedanych_bmw=suma_sprzedanych_bmw+srednia_liczba_sprzedanych_aut_bmw_w_miesiac 
        file.write(str(suma_sprzedanych_bmw)) 
        if(i<11):
            file.write(str(','))
with open("opel2.txt","w+") as file:
    for i in range(12):
        suma_sprzednaych_opli=suma_sprzednaych_opli+srednia_liczba_sprzedanych_aut_opel_w_miesiac
        file.write(str(suma_sprzednaych_opli))
        if(i<11):
            file.write(str(','))
with open("ford2.txt","w+") as file:
    for i in range(12):
        suma_sprzedanych_fordow=suma_sprzedanych_fordow+srednia_liczba_sprzedanych_aut_ford_w_miesiac
        file.write(str(suma_sprzedanych_fordow))
        if(i<11):
            file.write(str(','))
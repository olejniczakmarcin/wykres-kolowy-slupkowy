import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

print("Podaj pięć czynności jakie wykonywałeś w ciągu ostatniego dnia i czas jej trwania w godzinach")
czynnosc1 = input("pierwsza czynność(najdłuższa): ")
czas_wykonania1=float(input("podaj czas wykonania tej czynności: "))
czynnosc2=input("druga czynność: ")
czas_wykonania2=float(input("podaj czas wykonania tej czynności: "))
czynnosc3=input("trzecia czynność: ")
czas_wykonania3=float(input("podaj czas wykonania tej czynności: "))
czynnosc4=input("czwarta czynność: ")
czas_wykonania4=float(input("podaj czas wykonania tej czynności: "))
czynnosc5=input("piąta czynność: ")
czas_wykonania5=float(input("podaj czas wykonania tej czynności: "))

table=[czynnosc1,czynnosc2,czynnosc3,czynnosc4,czynnosc5]
table2=[float(czas_wykonania1),float(czas_wykonania2),float(czas_wykonania3),float(czas_wykonania4),float(czas_wykonania5)]

explode = (0.3, 0, 0, 0,0)
colors=['white','green','blue','orange','yellow']
fig1, ax1 = plt.subplots()
patches, texts, autotexts=ax1.pie(table2, explode=explode, labels=table, autopct='%1.1f%%',
        radius=5,colors=colors, shadow=True, startangle=90,textprops={'fontsize': 14})

texts[0].set_fontsize(16)
texts[1].set_fontsize(16)
texts[2].set_fontsize(16)
texts[3].set_fontsize(16)
texts[4].set_fontsize(16)
ax1.axis('equal')
ax1.legend(table,bbox_to_anchor=(0.1, 1.17), shadow=True)
plt.title('WYKRES',x = 0.50 ,y = 1.00, fontsize = 18,color = 'black')
fig1.patch.set_facecolor('xkcd:pink')
plt.show()
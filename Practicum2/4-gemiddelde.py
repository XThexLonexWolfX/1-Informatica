"""

auteur : Joosen Yorben
groep : PR09
datum : 04/10/2019

"""
aantal_ingelezen = 0
som = 0
gemiddelde = 0
getal = int(input('Geef een waarde voor getal (0 om te stoppen): '))
while getal != 0:
    aantal_ingelezen += 1
    som += getal
    getal = int(input('Geef een waarde voor getal (0 om te stoppen): '))
gemiddelde = som / aantal_ingelezen
print("Het aantal ingelezen getallen is:", aantal_ingelezen)
print('De som van de ingelezen getallen is:', som)
print('Het gemiddelde van de ingelezen getallen is:', gemiddelde)



"""
Auteur: Yorben Joosen
Groep: PR09
Datum: 22/11/2019
"""
from matplotlib import pyplot


def getallen_lezen(bestandnaam):
    bestand = open(bestandnaam)
    lijnen = bestand.readlines()
    bestand.close()
    lijst = []
    for lijn in lijnen:
        lijst.append(int(lijn.strip()))
    return lijst


lijst = getallen_lezen('getallen.txt')
frequentie = dict()
print(lijst)
for i in range(len(lijst)):
    if lijst[i] in frequentie:
        frequentie[lijst[i]] += 1
    else:
        frequentie[lijst[i]] = 1

pyplot.figure().canvas.set_window_title('Frequentietabel getallen')
pyplot.title('Frequentietabel van de getallen in bestand "gegevens.txt"')
pyplot.bar(frequentie.keys(), frequentie.values(), width=0.5) # maak staafdiagram voor 2018 met breedte 0.5
pyplot.show()

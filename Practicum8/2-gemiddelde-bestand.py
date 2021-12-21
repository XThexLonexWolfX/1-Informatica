"""
Auteur: Yorben Joosen
Groep: PR09
Datum: 22/11/2019
"""
from random import randint


def vul_bestand_met_getallen(bestandnaam, aantal, onder, boven):
    bestand = open(bestandnaam, 'w')
    for i in range(aantal):
        bestand.write('{:d}\n'.format(randint(onder, boven)))
    bestand.close()


def druk_bestand(bestandnaam):
    bestand = open(bestandnaam)
    buffer = bestand.read()
    bestand.close()
    print(buffer)


def gemiddelde_getallen_met_getallen(bestandnaam):
    bestand = open(bestandnaam)
    lijnen = bestand.readlines()
    bestand.close()
    lijst = []
    for lijn in lijnen:
        lijst.append(int(lijn.strip()))
    gemiddelde = sum(lijst) / len(lijst)
    print('lijst:', lijst)
    print('aantal:', len(lijst))
    print('som:', sum(lijst))
    print('gemiddelde', gemiddelde)
    return lijst


vul_bestand_met_getallen('getallen.txt', 100, 10, 30)
druk_bestand('getallen.txt')
gemiddelde_getallen_met_getallen('getallen.txt')
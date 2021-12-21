"""
Auteur: Yorben Joosen
Groep: PR06
Datum: 16/11/2019
"""
import datetime
from random import randint
import random


def doe_trekking():
    i = 0
    n = 0
    getallen = []
    sterren = []
    trekking = dict()
    trekking['datum'] = datetime.date.today()
    frequentie = dict()
    while i < 5:
        getallen.append(randint(1, 50))
        if getallen[n] in frequentie:
            frequentie[getallen[n]] += 1
            del getallen[n]
        else:
            frequentie[getallen[n]] = 1
            i += 1
            n += 1
    trekking['getallen'] = getallen
    frequentie = dict()
    i = 0
    n = 0
    while i < 2:
        sterren.append(randint(1, 12))
        if sterren[n] in frequentie:
            frequentie[sterren[n]] += 1
            del sterren[n]
        else:
            frequentie[sterren[n]] = 1
            i += 1
            n += 1
    trekking['sterren'] = sterren
    trekking['joker'] = '%0.6d' % random.randint(0, 999999)
    return trekking


def druk(trekking):
    print('Getallen: ', trekking['getallen'])
    print('Sterren: ', trekking['sterren'])
    print('Joker: ', trekking['joker'])


trekking = doe_trekking()
print('trekking:', trekking)
druk(trekking)


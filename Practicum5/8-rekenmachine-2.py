"""
auteur: Yorben Joosen
groep: PR09
datum: 16/11/2019
"""

import string
import math


def enkel_cijfers(s):
    allemaal_cijfers = True
    i = 0
    s = s.lstrip('-+')
    s = s.replace('.', '')
    if s == '':
        allemaal_cijfers = False
    while i < len(s) and allemaal_cijfers:
        allemaal_cijfers = s[i] in string.digits
        i += 1
    return allemaal_cijfers


def rekenmachine():
    print('getal1 =', getal1, '   getal2 =', getal2)
    print('0 verwissel getal1 en getal2')
    print('1 lees getal1')
    print('2 lees getal2')
    print('+ som')
    print('- verschil')
    print('* product')
    print('/ quotiënt')
    print('sin sinus')
    print('cos cosinus')
    print('vkw vierkantswortel')
    print('macht machtsverheffing')
    print('modulo rest_bij_deling')
    print('s stoppen')


getal1 = 0.0
getal2 = 0.0
keuze = 0
rekenmachine()
keuze = input('Maak keuze: ')
while keuze != 's':
    if keuze == '+':
        getal1 += getal2
        rekenmachine()
        keuze = input('Maak keuze: ')
    elif keuze == '-':
        getal1 -= getal2
        rekenmachine()
        keuze = input('Maak keuze: ')
    elif keuze == '*':
        getal1 *= getal2
        rekenmachine()
        keuze = input('Maak keuze: ')
    elif keuze == '/':
        getal1 /= getal2
        rekenmachine()
        keuze = input('Maak keuze: ')
    elif keuze == 'sin':
        getal1 = math.sin(getal2)
        rekenmachine()
        keuze = input('Maak keuze: ')
    elif keuze == 'cos':
        getal1 = math.cos(getal2)
        rekenmachine()
        keuze = input('Maak keuze: ')
    elif keuze == 'vkw':
        getal1 = getal1**(1/getal2)
        rekenmachine()
        keuze = input('Maak keuze: ')
    elif keuze == 'macht':
        getal1 = getal1 ** getal2
        rekenmachine()
        keuze = input('Maak keuze: ')
    elif keuze == 'modulo':
        getal1 = getal1 % getal2
        rekenmachine()
        keuze = input('Maak keuze: ')
    elif int(keuze) == 0:
        getal1, getal2 = getal2, getal1
        rekenmachine()
        keuze = input('Maak keuze: ')
    elif int(keuze) == 1:
        tester1 = input('Geef waarde voor getal1: ')
        if enkel_cijfers(tester1):
            getal1 = float(tester1)
        else:
            print('Geen float getal!')
            getal1 = float(input('Geef waarde voor getal1: '))
        rekenmachine()
        keuze = input('Maak keuze: ')
    elif int(keuze) == 2:
        tester2 = input('Geef waarde voor getal2: ')
        if enkel_cijfers(tester2):
            getal2 = float(tester2)
        else:
            print('Geen float getal!')
            getal2 = float(input('Geef waarde voor getal2: '))
        rekenmachine()
        keuze = input('Maak keuze: ')
    else:
        print('Dit is geen van de mogelijkheden')
        keuze = input('Maak keuze: ')
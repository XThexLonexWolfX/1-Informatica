"""
auteur: Yorben Joosen
groep: PR09
datum: 15/11/2019
"""
import string


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


def lees_float(onder, boven):
    getal_string = input('Geef getal tussen ' + str(onder) + ' en ' + str(boven) + ': ')
    while not enkel_cijfers(getal_string) or not (onder <= float(getal_string) <= boven):
        print('Geen float getal of buiten bereik!')
        getal_string = input('Geef getal tussen ' + str(onder) + ' en ' + str(boven) + ': ')
    print('Uitgevoerd: lees_float_getal(', onder, ',', boven, '):', float(getal_string))


lees_float(-10.0, 10.0)
lees_float(0.5, 2.5)

"""
auteur: Yorben Joosen
groep: PR09
datum: 25/10/2019
"""
import string


def enkel_cijfers(s):
    allemaal_cijfers = True
    i = 0
    while i < len(s) and allemaal_cijfers:
        s = s.lstrip('-+')
        allemaal_cijfers = s[i] in string.digits
        i += 1
    return allemaal_cijfers


def lees_geheel_getal(onder, boven):
    getal_string = input('Geef getal tussen ' + str(onder) + ' en ' + str(boven) + ': ')
    while not enkel_cijfers(getal_string) or not (onder <= int(getal_string) <= boven):
        print('Geen geheel getal of buiten bereik!')
        getal_string = input('Geef getal tussen ' + str(onder) + ' en ' + str(boven) + ': ')
    print('Uitgevoerd: lees_geheel_getal(', onder, ',', boven, '):', getal_string)
    return int(getal_string)


lees_geheel_getal(-10, -5)
lees_geheel_getal(-5, 5)
lees_geheel_getal(5, 10)


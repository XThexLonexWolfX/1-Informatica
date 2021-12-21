"""
Auteur: Yorben Joosen
Groep: PR06
Datum: 15/11/2019
"""


def lees_artikels():
    artikels = dict()
    artikelnaam = input('Geef artikelnaam (<Enter> stop): ')
    while artikelnaam != '':
        artikels[artikelnaam] = int(input('Geef aantal: '))
        artikelnaam = input('Geef artikelnaam (<Enter> stop): ')
    print('artikels:', artikels)8
    print('artikelnaam aantal')
    for key in artikels.keys():
        print(key, end=' ' * (18 - len(key) - len(str(artikels[key]))))
        print(artikels[key])
    print('artikelnaam aantal')
    for key in sorted(artikels):
        print(key, end=' ' * (18 - len(key) - len(str(artikels[key]))))
        print(artikels[key])
    artikelnaam = input('Geef artikelnaam (<Enter> stop): ')
    while artikelnaam != '':
        if artikelnaam in artikels.keys():
            print('Er zijn', artikels[artikelnaam], artikelnaam, 'aanwezig.')
        else:
            print('Dit product is niet aanwezig, probeer opnieuw')
        artikelnaam = input('Geef artikelnaam (<Enter> stop): ')
    return artikels


lees_artikels()

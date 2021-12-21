"""
Auteur: Yorben Joosen
Groep: PR06
Datum: 15/11/2019
"""


def lees_artikels():
    artikels1 = dict()
    artikels2 = dict()
    print('Lees artikels1:')
    artikelnaam1 = input('Geef artikelnaam (<Enter> stop): ')
    while artikelnaam1 != '':
        artikels1[artikelnaam1] = int(input('Geef aantal: '))
        artikelnaam1 = input('Geef artikelnaam (<Enter> stop): ')
    print('Lees artikels2:')
    artikelnaam2 = input('Geef artikelnaam (<Enter> stop): ')
    while artikelnaam2 != '':
        artikels2[artikelnaam2] = int(input('Geef aantal: '))
        artikelnaam2 = input('Geef artikelnaam (<Enter> stop): ')
    print('artikels1:', artikels1)
    print('artikels2:', artikels2)
    print('artikels1:')
    print('artikelnaam aantal')
    for key in artikels1.keys():
        print(key, end=' ' * (18 - len(key) - len(str(artikels1[key]))))
        print(artikels1[key])
    print('artikels2:')
    print('artikelnaam aantal')
    for key in artikels2.keys():
        print(key, end=' ' * (18 - len(key) - len(str(artikels2[key]))))
        print(artikels2[key])
    artikels3 = artikels1.copy()
    artikels3.update(artikels2)
    for key in artikels1.keys() and artikels2.keys():
        if key in artikels1.keys() and artikels2.keys():
            artikels3[key] += artikels1[key]
        else:
            artikels3[key] = artikels3[key]
    print('artikels3:', artikels3)
    print('artikels3:')
    for key in artikels3.keys():
        print(key, end=' ' * (18 - len(key) - len(str(artikels3[key]))))
        print(artikels3[key])
    print('artikels3 gesorteerd:')
    for key in sorted(artikels3):
        print(key, end=' ' * (18 - len(key) - len(str(artikels3[key]))))
        print(artikels3[key])


lees_artikels()

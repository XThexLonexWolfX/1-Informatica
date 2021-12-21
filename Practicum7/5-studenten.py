"""
Auteur: Yorben Joosen
Groep: PR06
Datum: 15/11/2019
"""


def lees_studenten():
    lijst = []
    st = dict()
    st['naam'] = input('Geef naam (<Enter> stop): ')
    while st['naam'] != '':
        st['opleiding'] = input('Geef opleiding (BK,CH,EI,EM): ')
        st['resultaat'] = int(input('Geef resultaat (0-100): '))
        lijst.append(st)  # voeg student dictionary toe aan lijst
        st = dict()  # lege dictionary om de studentengegevens in te lezen
        st['naam'] = input('Geef naam (<Enter> stop): ')
    return lijst


def graad(resultaat):
    if 50 <= resultaat <= 64:
        print('voldoende wijze')
    elif 65 <= resultaat <= 74:
        print('onderscheiding')
    elif 75 <= resultaat <= 84:
        print('grote onderscheiding')
    else:
        print('grootste onderscheiding')


studenten = lees_studenten()
print('studenten:\n', studenten)
print('naam    opleiding resultaat  graad')
for i in studenten:
    print(i['naam'], end=' ' * (14 - len(i['naam']) - len(i['opleiding'])))
    print(i['opleiding'], end=' ' * (13 - len(i['opleiding'])))
    print(i['resultaat'], end='  ')
    graad(i['resultaat'])
print('volgens_opleiding_resultaat(studenten):')
print('naam    opleiding resultaat  graad')
gesorteerd_opleiding_resultaat = sorted(studenten, key=lambda i: (i['opleiding'].lower(), i['resultaat']))
for i in gesorteerd_opleiding_resultaat:
    print(i['naam'], end=' ' * (14 - len(i['naam']) - len(i['opleiding'])))
    print(i['opleiding'], end=' ' * (13 - len(i['opleiding'])))
    print(i['resultaat'], end='  ')
    graad(i['resultaat'])

"""
Auteur: Yorben Joosen
Groep: PR06
Datum: 17/11/2019
"""
from random import randint


def vulmatrix(dimrij, dimkolom, onder, boven):
    m = [['+']+['-']*dimkolom+['+']]
    for i in range(1, dimrij+1):
        m.append(['|'])
        for j in range(dimkolom):
            waarde = randint(onder, boven)
            if waarde == 1:
                m[i].append('X')
            else:
                m[i].append(' ')
        m[i].append('|')
    m.append(['+']+['-']*dimkolom+['+'])
    return m


def drukmatrix(titel, m):
    print(titel+': ('+str(len(m)-2)+'x'+str(len(m[0])-2)+')')
    for i in range(len(m)):
        for j in range(len(m[i])):
            print('{:1s}'.format(m[i][j]), end='',)
        print('')


def tel_levend(m, i, j):
    teller = 0
    for k in range(i-1, i+2):
        for l in range(j-1, j+2):
            if k != i or l != j:
                if m[k][l] == 'X':
                    teller += 1
    return teller


def volgende_generatie(m):
    g = []
    for i in range(len(m)):
        g.append([])
        for j in range(len(m[0])):
            if m[i][j] == 'X':
                omliggenden = tel_levend(m, i, j)
                if omliggenden == 2 or omliggenden == 3:
                    g[i].append('X')
                else :
                    g[i].append(' ')
            elif m[i][j] == ' ':
                omliggenden = tel_levend(m, i, j)
                if omliggenden == 3:
                    g[i].append('X')
                else:
                    g[i].append(' ')
            else:
                g[i].append(m[i][j])
    return g


def game_of_life(aantalgeneraties):
    generatie = vulmatrix(14, 14, 1, 4)
    drukmatrix('Game of life', generatie)
    for gen in range(aantalgeneraties-1):
        afstammelingen = volgende_generatie(generatie)
        drukmatrix('generatie '+str(gen+2), afstammelingen)
        generatie = afstammelingen


aantalgeneraties = int(input('Aantal generaties (0 om te stoppen): '))
while aantalgeneraties != 0:
    game_of_life(aantalgeneraties)
    aantalgeneraties = int(input('Aantal generaties (0 om te stoppen): '))
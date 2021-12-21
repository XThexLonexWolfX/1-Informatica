"""
Auteur: Yorben Joosen
Groep: PR06
Datum: 16/11/2019
"""

zin = input('Geef een zin: ')
print('zin:', zin)
woorden = zin.split()
print('woorden:', woorden)
frequentie = dict()
for i in woorden:
    if i in frequentie:
        frequentie[i] += 1
    else:
        frequentie[i] = 1
print('frequentie: ', frequentie)
print('woorden  aantal')
for key in sorted(frequentie):
    print(key, end=' ' * (15 - len(key) - len(str(frequentie[key]))))
    print(frequentie[key])

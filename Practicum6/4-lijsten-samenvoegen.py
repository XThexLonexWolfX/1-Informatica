"""
Auteur: Yorben Joosen
Groep: PR06
Datum: 08/11/2019
"""


def lees_lijst(aantal):
    lijst = []
    for i in range(aantal):
        getal = int(input('Geef getal '+str(i+1)+' : '))
        lijst.append(getal)
    return lijst


print('Inlezen lijst 1')
lijst1 = lees_lijst(4)

print('Inlezen lijst 2')
lijst2 = lees_lijst(3)
print('lijst1: ', lijst1)
print('lijst2: ', lijst2)
lijst3 = lijst1 + lijst2
print('lijst3: ', lijst3)
print('lijst3: ', sorted(lijst3,reverse=True))

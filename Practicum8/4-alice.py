"""
Auteur: Yorben Joosen
Groep: PR09
Datum: 22/11/2019
"""

def enkel_cijfers(s):
    return any(i.isdigit() for i in s)


def genereer_woordfrequentie_dictionairy(bestandnaam):
    lijst = []
    Teller = 0
    frequentie = dict()
    bestand = open(bestandnaam)
    for line in bestand:
        for word in line.split():
            lijst.append(word)
    bestand.close()
    for i in range(len(lijst)):
        if enkel_cijfers(lijst[i]) is False:
            if lijst[i] in frequentie:
                frequentie[lijst[i]] += 1
            else:
                frequentie[lijst[i]] = 1
    for key in sorted(frequentie):
        print(key, frequentie[key])
    gesorteerd = dict(sorted(frequentie.items(), key=lambda i: i[1], reverse=True))
    for i in gesorteerd:
        if Teller < 16:
            print(i, gesorteerd[i])
            Teller += 1
    #print(frequentie)
    #print(lijst)


genereer_woordfrequentie_dictionairy('alice.txt')

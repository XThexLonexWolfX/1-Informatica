"""
Auteur: Yorben Joosen
Groep: PR09
Datum: 17/01/2020
"""


class Wim:
    voertuigtype_str = ['PR', 'LV', 'VR', 'ZV']

    def __init__(self):
        self.__gegevens = dict()

    def voegtoe(self, datum, type):
        if datum in self.__gegevens:
            if type in self.__gegevens[datum]:
                self.__gegevens[datum][type] += 1
            else:
                self.__gegevens[datum][type] = 1
        else:
            self.__gegevens[datum] = {type: 1}

    def rapport(self):
        rapport = 'Wim rapport:\n'
        for datum in sorted(self.__gegevens):
            rapport += datum + '\n'
            rapport += '\t' + str(type) + ' (' + Wim.voertuigtype_str[type] + ') : ' + \str(self.__gegevens[datum][type]) + '\n'
        return rapport

def main():
    print('Verwerken van wim-gegevens:')
    wimgegevens = Wim()
    with open('voertuigen.txt') as voertuigenfile:
        voertuig = voertuigenfile.readline()
        while voertuig != '':
            data = voertuig.strip().split(';')
            if data[0] == 'Antw':
                wimgegevens.voegtoe(data[1], int(data[2]))
            voertuig = voertuigenfile.readline()
    print(wimgegevens.rapport())
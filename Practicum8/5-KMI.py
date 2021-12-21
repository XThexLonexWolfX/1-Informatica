"""
Auteur: Yorben Joosen
Groep: PR09
Datum: 17/12/2019
"""
from matplotlib import pyplot


def lees_en_converteer_temperatuur_csv_bestand(bestandnaam):
    temperatuurfile = open(bestandnaam)
    temperatuurfilelist = temperatuurfile.readlines()
    temperatuurfile.close()
    temperatuurlist = []
    jaarlijst = []
    jaargemiddelde = []
    som = 0
    for jaardata in temperatuurfilelist:
        data = jaardata.strip().split(';')
        temperatuurlist.append(data)
    for i in range(len(temperatuurlist)):
        for j in range(len(temperatuurlist[i])):
            if j == 0:
                temperatuurlist[i][j] = int(temperatuurlist[i][j])
            elif len(temperatuurlist[i][j]) > 0:
                temperatuurlist[i][j] = float(temperatuurlist[i][j])
            else:
                temperatuurlist[i][j] = 0.0
    for i in range(6):
        jaarlijst.append(temperatuurlist[i][0])
    for i in range(6):
        for j in range(1,13):
            som += temperatuurlist[i][j]
        gemiddelde = som / 12
        jaargemiddelde.append(gemiddelde)
        som = 0
    print(jaargemiddelde)
    print(jaarlijst)
    print(temperatuurlist)
    pyplot.figure().canvas.set_window_title('Gemiddelde jaartemperaturen')
    pyplot.title('Overzicht gemiddelde temperatuur per jaar')
    for i in range(6):
        pyplot.bar(jaarlijst[i], jaargemiddelde[i], width=0.5)
    pyplot.show()
    return temperatuurlist


lees_en_converteer_temperatuur_csv_bestand('KMI-temperatuur.csv')

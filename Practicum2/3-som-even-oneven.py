"""

auteur : Joosen Yorben
groep : PR09
datum : 04/10/2019

"""

aantal = int(input('Geef een waarde voor aantal: '))
som_even = 0
som_oneven = 0
n = 1
for i in range(1,aantal + 1):
    getal = int(input('Geef getal '+ str(n) + ': '))
    n += 1
    if getal % 2 == 0:
        som_even += getal
    else:
        som_oneven += getal
print('De som van de even getallen:', som_even)
print('De som van de oneven getallen:', som_oneven)

"""
Auteur: Yorben Joosen
Groep: PR09
Datum: 22/11/2019
"""

set1 = set()
set2 = set()
set3 = set()
set4 = set()
for i in range(1, 71):
    if i % 2 == 0:
        set1.add(i)  # of set = (range(2, 71, 2))
    if i % 3 == 0:
        set2.add(i)
    if i % 5 == 0:
        set3.add(i)
    set4.add(i)
print('Alle getallen tussen 1 en 70 die deelbaar zijn door 2:\n', set1)
print('Alle getallen tussen 1 en 70 die deelbaar zijn door 3:\n', set2)
print('Alle getallen tussen 1 en 70 die deelbaar zijn door 5:\n', set3)
print('Alle getallen tussen 1 en 70:\n', set4)
print('Alle getallen tussen 1 en 70 die niet deelbaar zijn door 2, niet door 3 en niet door 5:\n', set4.difference(set1).difference(set2).difference(set3))
print('Alle getallen tussen 1 en 70 die deelbaar zijn door 2 maar niet door 3 en niet door 5:\n', set1.difference(set2).difference(set3))
print('Alle getallen tussen 1 en 70 die deelbaar zijn door 2 en 3 maar niet door 5:\n', set1.intersection(set2).difference(set3))
print('Alle getallen tussen 1 en 70 die deelbaar zijn door 2, 3 en 5:\n', set1.intersection(set2, set3))

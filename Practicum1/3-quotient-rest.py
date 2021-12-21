"""
auteur: Joosen Yorben
groep: PR09
datum: 29/09/2019

Inlezen van twee getallen en de gehele deling en rest afdrukken
"""
deeltal = int(input('Geef deeltal: '))
deler = int(input('Geef deler: '))
gehele_deling = deeltal//deler
rest= deeltal%deler
print('Het quotiënt is', gehele_deling)
print('De rest is', rest)
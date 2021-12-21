"""
auteur: Yorben Joosen
groep: PR09
datum: 25/10/2019
"""
naam = input('Geef uw voornaam: ')
n = 0
while n <= len(naam) + - 1:
    print('naam[' + str(n) + ']', naam[n], 'met als ASCII-code', ord(naam[n]))
    n += 1

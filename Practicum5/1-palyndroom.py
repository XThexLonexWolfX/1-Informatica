"""
auteur: Yorben Joosen
groep: PR09
datum: 25/10/2019
"""
def is_palindroom(woord):
    palindroom = True
    voor = 0
    achter = len(woord) - 1
    while palindroom and voor < achter:
        palindroom = woord[voor] == woord[achter]
        voor += 1
        achter -= 1
    return palindroom


woord = input('Geef een woord (stop om te stoppen): ')
while woord != 'stop':
    if is_palindroom(woord) == False:
        print(woord, 'is geen palyndroom')
    else:
        print(woord, 'is een palyndroom')
    woord = input('Geef een woord (stop om te stoppen): ')
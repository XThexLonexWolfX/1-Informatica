n = 1
getal = int(input('Geef getal: '))
while n > 0:
    n = getal % 10
    print(n)
    getal -= n
    getal /= 10
    print(getal)

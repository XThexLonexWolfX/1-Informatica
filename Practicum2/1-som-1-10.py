"""

auteur : Joosen Yorben
groep : PR09
datum : 04/10/2019

"""

n = 10
som = 0
teller = 1
while teller <= n:
    som += teller
    teller += 1
print('Met while: De som van de getallen 1 tot 10 is', som)
som = 0
for i in range(1,11):
    som += i
print('Met for: De som van de getallen 1 tot 10 is', som)
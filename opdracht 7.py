""" Opdracht 7 - Random """

import random
gokindex = 0

print("Hello ! wat is uw naam ? ")
name = input()

nummer = random.randint(1, 100)
print("Well ! {} Ik denk aan een getal tussen 1 en 100 !".format(name))

while gokindex < 7:
    print(" Gok maar ! ")
    gok = int(input())
    gokindex += 1
    if gok < nummer:
        print("Uw gok is laag ! ")
    if gok > nummer :
        print("uw gok is hoog!")
    if gok == nummer :
        break
if gok == nummer:
    print(" Goed gedaan {}! u heeft mijn nummer gevonden in {} keer ".format(name,gokindex))

if gok != nummer :
    print("Sorry {} ! {} was het getal waar ik aan dacht :(. Game Over  ".format(name , nummer))

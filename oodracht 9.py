"""Opdracht 9 - Cyclisch verschuiven """


def verchuiven(ch , n):
    for bitje in range(len(str(ch))) :
        for i in range(bitje) :
            if n > 0 :
                return ch[n:] + ch[:n]
            elif n < 0 :
                return ch[:n] + ch[n:]




print(verchuiven("1011000",3))




"""Opdracht 6 - Gemiddelde berekenen """


def gemiddelde(lst):
    lst = sorted(lst)
    A = int(len(lst))
    for i in range(len(lst)):
        B = sum(lst)
    C = B / A
    return C
lst = []
n = int(input("voer gewilde aantal elementen in : \n"))
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
print("uw list is \n " , lst)
print(f"uw gemiddeld is \n " , gemiddelde(lst))
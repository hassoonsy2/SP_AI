""" Opdracht 1 - Pyramide """


I = int(input("Hoe groot ? "))
x = "*"


for ster in range(1 , I+1):
    for y in range(1, ster+1):
        print(x, end=" ")
    print(" ")

index = 0
for ster in range(I , -1 , -1):
    index += 1
    for j in range(0, ster+1):
        print(x , end=" ")
    print(" ")


u = 1
while u <= I :
    t = 1
    while t <= u :
        print((x), end=" ")
        t = t +1
    u = u +1
    print(" ")

u = 1
while u <= I :
    t = I
    while t >= u:
        print(x , end= " ")
        t -= 1
    u = u + 1
    print(" ")

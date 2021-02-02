""" Opdracht 3 - Lijstcheck """

"""A"""
def count1(lst, x):
    return lst.count(x)
print("A.\n")
lst1 = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print('{} voorkomt in de list {} keer'.format(x, count1(lst1, x)))


"""B"""
def groste_verschil(lst, Y):
    groste_verschil = lst[0] - lst[1]
    for i in range(0 , y):
        for j in range(i +1 , y):
            if(lst[j] - lst[i]> groste_verschil):
                groste_verschil = lst[j] - lst[i]
    return groste_verschil
lst = [1,2,4,7,7,4]
y = len(lst)
print("B. \n")
print ("Het groste verschil is", groste_verschil(lst, y))

"""C"""

def do_somthing(lst):
    nul = count1(lst,0)
    een = count1(lst,1)
    if nul >= 12 :
        return print('{} voorkomt in de list {} keer er mag minmaal\n 12 keer voorkomen'.format(0, nul))
    elif een > nul:
        return print('{} voorkomt in de list {} keer'.format(1, een))
    else:
        return print('{} voorkomt in de list {} keer'.format(0, nul))

lst = [0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,0,0,0,0]
print("C. \n")
do_somthing(lst)






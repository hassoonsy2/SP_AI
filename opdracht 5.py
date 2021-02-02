""" Opdracht 5 - Sorteren """


def sorteren(lst):
    lst_sorted = lst.copy()
    index = 0
    n = len(lst_sorted)
    while index != n:
        already_sorted = True
        for i in range(n - 1):
            if int(lst_sorted[i]) > int(lst_sorted[i + 1]):
                lst_sorted[i], lst_sorted[i + 1] = lst_sorted[i + 1], lst_sorted[i]
                already_sorted = False
        if already_sorted:
            break
        index += 1

    return lst_sorted


lst=[4,9,3,5,8,2]
x = sorteren(lst)
print(x)
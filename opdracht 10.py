def finbonacci(n):
    if n < 0 :
        print("nummer mag niet lager dan  0 zijn")

    elif n == 0 :
        return 0

    elif n == 1 or n== 2:
        return 1

    else:
        return finbonacci(n-1) + finbonacci(n-2)


n = int(input(" voer een nummer in ! "))
print(finbonacci(n))
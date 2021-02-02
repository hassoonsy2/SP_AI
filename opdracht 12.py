""" Opdracht 12 - FizzBuzz """


def Fizzbuzz():
    for fizzbuzz in range(100):
        if fizzbuzz % 15 == 0 :
            print("FizzBuzz!")
            continue
        elif fizzbuzz % 3 == 0 :
            print("fizz")
            continue
        elif fizzbuzz % 5 == 0:
            print("Buzz")
            continue
        print(fizzbuzz)

    return fizzbuzz



print(Fizzbuzz())
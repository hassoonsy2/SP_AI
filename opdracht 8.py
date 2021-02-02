""" Opdracht 8 - Compressie """

lst =[]
x = open("opdracht 8 1.txt", "r+")
for letter in x.read():
    if letter == " ":
        letter = ""
        lst.append(letter)
    elif letter == "\n":
        letter = ""
        lst.append(letter)
    elif letter == ".":
        letter = ""
        lst.append(letter)
    elif letter == "\t":
        letter = ""
        lst.append(letter)
    elif letter == ",":
        letter = ""
        lst.append(letter)

    else:
        lst.append(letter)


y = open("opdracht 8 2.txt", "w+")

y.writelines(lst)















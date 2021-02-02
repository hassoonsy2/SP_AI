""" Opdracht 4 - Palindroom """

def palindroom(x):
    return x == x[::-1]

x = "malayalam"
y = palindroom(x)
if (y):
    print(True)
else:
    print(False)
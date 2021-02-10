""" MasterMind

   Hussin ALmoustafa   """




import random




colors = ["A", "B", "C", "D", "E", "F"]



def Aantal_Moelijkhede():
    """ Een functie die alle kleuren combinatie in een list stopt """

    keys = "ABCDEF"
    arr = keys
    mogelijkheden = []
    for i in range(6):
        for j in range(6):
            for k in range(6):
                for m in range(6):
                    antwoord = arr[i] + arr[j] + arr[k] + arr[m]
                    mogelijkheden.append(antwoord)

    return mogelijkheden

def randomcode():
    """
         Een Functie die rondom combinatie geeft
    """
    mogelijkheden = Aantal_Moelijkhede()
    return random.choice(mogelijkheden)




def evaluate(gok, kleur_code):
        zwartepen, wittepen = 0, 0
        gokset, secretset = set([]), set([])
        for i in range(4):
            if gok[i] == kleur_code[i]:
                zwartepen = zwartepen + 1
            else:
                gokset.add(gok[i])
                secretset.add(kleur_code[i])

        return zwartepen, len(gokset.intersection(secretset))



def Simpel_strategy(kleur_code):
    print(""" Simpel Strategy """)
    vorige_gokken = []
    gok = randomcode()
    pogingen = 0
    while True:
        zwartepen, wittepen = evaluate(gok, kleur_code)
        vorige_gokken.append((gok, zwartepen, wittepen))
        print(gok, zwartepen, wittepen)
        if zwartepen == 4:
            break  
        pogingen = pogingen + 1

        while True:
            gok = randomcode()
            consistent = True
            for g, zwartepen, wittepen in vorige_gokken:
                nz, nw = evaluate(gok, g)
                if nz != zwartepen or nw != wittepen:
                    consistent = False
                    break
            if consistent:
                break
    return gok

def Worst_case_strategy(kleur_code):
    print(""" Worst Case Strategy """)


    vorige_gokken = []
    gok = randomcode()
    pogingen = 0
    if pogingen == 0:
        gok = "AABB"
        pogingen = pogingen + 1

    while pogingen != 0:
        zwartepen, wittepen = evaluate(gok, kleur_code)
        vorige_gokken.append((gok, zwartepen, wittepen))
        print(gok, zwartepen, wittepen)
        if zwartepen == 4:
            break  
        pogingen = pogingen + 1

        while True:
            gok = randomcode()
            consistent = True
            for g, zwartepen, wittepen in vorige_gokken:
                nz, nw = evaluate(gok, g)
                if nz != zwartepen or nw != wittepen:
                    consistent = False
                    break
            if consistent:
                break
    return gok


def Game():
    print(" --- MASTERMIND --- \n")
    print("Raad de geheime kleurcode in zo min mogelijk pogingen.\n")
    print("Voer uw kleurcode in. \n U kunt rood (A), groen (B), blauw (C), geel (D), wit (E) en roze (F) gebruiken")


    pogingen = 0
    spelen = True
    global kleur_code

    kleur_code = randomcode()
    print(kleur_code)

    while spelen:

        b, w = 0, 0
        gokeset, secretset = set([]), set([])

        speler_gok = Worst_case_strategy(kleur_code)


        pogingen += 1


        if len(str(speler_gok)) != len(kleur_code):

            print(
                "\nDe geheime code heeft precies vier kleuren. Ik weet het, je kunt tot vier tellen. Probeer het nog eens!")
            continue
        for i in range(4):
            if speler_gok[i] not in colors:
                print("\nZoek op welke kleuren je in dit spel kunt gebruiken !!!!")
                continue

        if b != 4 :
            for i in range(0, len(speler_gok)):
                if speler_gok[i] == kleur_code[i]:

                    b = b + 1
                elif speler_gok[i] != kleur_code[i] and speler_gok[i] in kleur_code :
                    gokeset.add(speler_gok[i])
                    secretset.add(kleur_code[i])
            feedback1 = b, len(gokeset.intersection(secretset))
            print(feedback1)
            print(speler_gok)

        if b == 4:
            if pogingen == 1:
                print("Wauw! Je raadt het al bij de eerste poging!")
                print("Gefsltieerd!!!! U heeft gewonen!")
            else:
                print("Goed gedaan... Binnen " + str(pogingen) + " Keer je raadt het al.")
                print("Gefsltieerd!!!! U heeft gewonen!")
            spelen = False

        if pogingen >= 1 and pogingen < 8 and b != 4:
            print("Volgende poging: ")
        elif pogingen >= 8:
            print("Je raadde het niet! De geheime kleurcode was: " + str(kleur_code))

        while spelen == False:
            finish_game = input("\nWil je nog een keer spelen (J / N)?").upper()
            pogingen = 0
            if finish_game == "N":
                print("Bedankt voor het spel! Tot ziens!")
                break
            elif finish_game == "J":
                spelen = True
                print("Dus laten we opnieuw spelen ... Raad de geheime code:")



Game()
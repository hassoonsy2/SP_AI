""" --- MASTERMIND --- """
import random

kleuren = ["A", "B", "C", "D", "E", "F"]








def aantal_moelijkhede():
    """ Een functie die alle kleuren combinatie in een list stopt """

    keys = "ABCDEF"
    arr = keys
    aantal_mogelijkheden = []
    for i in range(6):
        for j in range(6):
            for k in range(6):
                for m in range(6):
                    antwoord = arr[i] + arr[j] + arr[k] + arr[m]
                    aantal_mogelijkheden.append(antwoord)

    print(aantal_mogelijkheden)
    return aantal_mogelijkheden




def feedback_analyze(speler_gok , kleur_code ):
    """ Een functie die de evaluatie weergeeft.
     De evaluatie is als volgt:

    Als je een pin op de juiste plaats en in de juiste kleur hebt, dan krijg je een zwarte pin >> [1]
    Als je een pin op de verkeerde plaats hebt maar de juiste kleur, dan krijg je een witte pin >> [0]
     Anders krijg je >> [-1]"""

    feedback = [-1, -1, -1, -1]

    for i in range(len(kleur_code)):
        if  speler_gok[i] == kleur_code[i]:
            feedback[i] = 1
        elif speler_gok.count(kleur_code[i]) == 1:
            feedback[i] = 0
        else:
            feedback[i] = -1
    print(feedback)

    return feedback



def generate_random_move(kleur_code):
    """
    Generates a random move
    """
    move = []
    available_choices = ["A", "B", "C", "D", "E", "F"]


    for x in range(0, len(kleur_code)):
        val = random.choice(available_choices)
        move.append(val)
        available_choices.remove(val)
    print(move)

    return move

def een_conscistant_gok(gok, feedback):
    niewue_gok = []
    feedback = feedback_analyze(gok, kleur_code)
    for i in range(0, len(gok)):
        if feedback[i] == 1 :
            niewue_gok.append(gok[i])

        elif feedback[i] == 0:
            gok.split()
            print(gok.split("(?!^)"))
            gok[i] = gok.index()
            niewue_gok.append(gok[i])

    print(niewue_gok)
    return gok









def game():
    print(" --- MASTERMIND --- \n")
    print("Raad de geheime kleurcode in zo min mogelijk pogingen.\n")
    print("Voer uw kleurcode in. \n U kunt rood (A), groen (B), blauw (C), geel (D), wit (E) en roze (F) gebruiken")


    pogingen = 0
    spelen = True
    global kleur_code

    kleur_code = random.sample(kleuren, 4)
    print(kleur_code)

    while spelen:
        juiste_kleur = ""
        geraden_kleur = ""

        speler_gok = input().upper()
        pogingen += 1


        if len(speler_gok) != len(kleur_code):
            print(
                "\nDe geheime code heeft precies vier kleuren. Ik weet het, je kunt tot vier tellen. Probeer het nog eens!")
            continue
        for i in range(4):
            if speler_gok[i] not in kleuren:
                print("\nZoek op welke kleuren je in dit spel kunt gebruiken !!!!")
                continue

        if juiste_kleur != "****":
            for i in range(0, len(speler_gok)):
                if speler_gok[i] == kleur_code[i]:
                    juiste_kleur += "*"




                elif speler_gok[i] != kleur_code[i] and speler_gok[i] in kleur_code :
                    geraden_kleur += "."

            feedback = (juiste_kleur + geraden_kleur +"\n")
            print(feedback)

        if juiste_kleur == "****":
            if pogingen == 1:
                print("Wauw! Je raadt het al bij de eerste poging!")
                print("Gefsltieerd!!!! U heeft gewonen!")
            else:
                print("Goed gedaan... Binnen " + str(pogingen) + " Keer je raadt het al.")
                print("Gefsltieerd!!!! U heeft gewonen!")
            spelen = False

        if pogingen >= 1 and pogingen < 8 and juiste_kleur != "***":
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



game()

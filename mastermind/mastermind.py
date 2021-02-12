""" MasterMind

   Hussin ALmoustafa

   Studentennummer : 177645 """






import random




colors = ["A", "B", "C", "D", "E", "F"]



def Aantal_Moelijkhede():
    """ Een functie die alle kleuren combinatie in een list stopt """

    keys = colors
    mogelijkheden = []
    for i in range(6):
        for j in range(6):
            for k in range(6):
                for m in range(6):
                    antwoord = keys[i] + keys[j] + keys[k] + keys[m]
                    mogelijkheden.append(antwoord)
    #Hierbij return ik een alfabetisch gesorteerd lijst !
    return mogelijkheden


def randomcode():
    """
         Een Functie die rondom combinatie geeft
    """
    mogelijkheden = Aantal_Moelijkhede()
    return random.choice(mogelijkheden)


def Geef_een_Gok(vorge_gok):
    """
        Een functie die een gok truge geeft
    """
    mogelijk_goken = Aantal_Moelijkhede()
    for i in range(len(mogelijk_goken)):
        if mogelijk_goken[i] == vorge_gok :
            gok = mogelijk_goken[i + 1]
            break

    return gok




def evaluate(gok, kleur_code):
    """
        Een Fuctie die de gokken evalueren en de zwarte en de witte pennen treug geeft

    """

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

    """ Het Simpel Strategy werkt als volende :
    Eerst  geef ik de eerste gok vanuit Aantal moeglijkheden lijst
    Daarna krijg ik de Antwoord
    De gok en de antwoorden worden in de Vorige gokken lijst toegevoegd (om te kijken hoe consistent de vogende gok zou zijn)
    Als de Antwoord gelijk aan 4 :
      Dan stopt de algoritme
    Vogende gok is eigelijk de eerst vogende consistente gok van uit de Aantal moeglijkheden lijst
    Enzo  tot de comnputer de code raad

    """


    print("""==== Simpel Strategy==== """)
    print("=====(Gokken)===(Z)==(W)===== ")
    vorige_gokken = []
    #Hier bij beginen we met de eerste gok in de aantal moeglijkheden list
       #AAAA
    gok = Aantal_Moelijkhede()[0]
    pogingen = 0
    while True:
        zwartepen, wittepen = evaluate(gok, kleur_code)
        vorige_gokken.append((gok, zwartepen, wittepen))
        print(gok,"|",zwartepen,"| ", wittepen)
        if zwartepen == 4:
            #Break ! we hebben de gehaime code gevonden !
            break  
        pogingen = pogingen + 1

        while True:
            # genereer een nieuwe willekeurige gok, consistent met
            # alle eerdere gokken !.
            gok = Geef_een_Gok(gok)
            consistent = True
            for g, zwartepen, wittepen in vorige_gokken:
                # Hier wordt gekijken naar de evaluatie van de gok waarbij wordt vergelijkten om de vorigen gokken
                nz, nw = evaluate(gok, g)
                if nz != zwartepen or nw != wittepen:
                    consistent = False
                    break
            if consistent:
                break
    print("==========================")
    return gok, pogingen




def Worst_case_strategy(kleur_code):

    """ Het Worst case Strategy werkt als volende :
        Eerst geef ik de eerste gok altijd AABB om mijn Aantal moegelijkheden lijst te gaan beperken
        Daarna krijg ik de Antwoord
        De gok en de antwoorden worden in de Vorge gokken lijst toegevoegd (om te kijken hoe consistent de vogende gok zou zijn)
        Als de Antwoord gelijk aan 4 :
          Dan stopt de algoritme
        Vogende gok is eigelijk de eerst vogende consistente gok van uit de Aantal moeglijkheden lijst
        Enzo blijft tot de comnputer de code raad

        """
    print("""=== Worst Case Strategy ===""")
    print("=====(Gokken)===(Z)==(W)===== ")
    vorige_gokken = []
    gok = Aantal_Moelijkhede()[0]
    pogingen = 0
    if pogingen == 0:
        #We beginen Altijd met de gok AABB dan wordt mijn lijst met aantalmoegelijkheden worstcase (256) over

        gok = "AABB"
        pogingen = pogingen + 1

    while pogingen != 0:
        zwartepen, wittepen = evaluate(gok, kleur_code)
        #Na de evaluatie wordt de gok , zwarte en de witten pennen toegoevoeged aan de vorige gokken lijst
        vorige_gokken.append((gok, zwartepen, wittepen))
        print(gok,"|",zwartepen,"| ", wittepen)
        if zwartepen == 4:
            # Break ! we hebben de gehaime code gevonden !
            break  
        pogingen = pogingen + 1
        while True:
            # genereer een nieuwe willekeurige gok, consistent met
            # alle eerdere gokken !.
            gok = Geef_een_Gok(gok)
            consistent = True
            for g, zwartepen, wittepen in vorige_gokken:
                #Hier wordt gekijken naar de evaluatie van de gok waarbij wordt vergelijkten om de vorigen gokken
                nz, nw = evaluate(gok, g)
                if nz != zwartepen or nw != wittepen:
                    consistent = False
                    break
            if consistent:
                break
    print("==========================")
    return gok , pogingen




def Eigen_Strategy(kleur_code):


    """ Het Eien Strategy werkt als volende :
           Eerst geef ik de eerste gok altijd ABCD om mijn Aantal moegelijkheden lijst te gaan beperken met 312 elmenten over in het worst case
           Daarna krijg ik de Antwoord
           De gok en de antwoorden worden in de Vorge gokken lijst toegevoegd (om te kijken hoe consistent de vogende gok zou zijn)
           Als de Antwoord gelijk aan 4 :
             Dan stopt de algoritme
           Als de Antwoord gelijk aan 0 :
             Dan verwijder ik de element van Aantal mogelijkheden lijst
           Vogende gok is eigelijk de eerst vogende consistente gok van uit de Aantal moeglijkheden lijst
           Enzo blijft tot de comnputer de code raad

           """

    print("====Eigen Strategy=====")
    print("=====(Gokken)===(Z)==(W)===== ")
    vorige_gokken = []
    gok = Aantal_Moelijkhede()[0]
    pogingen = 0
    if pogingen == 0:
        gok = "ABCD"
        pogingen = pogingen + 1


    while pogingen != 0:

        zwartepen, wittepen = evaluate(gok, kleur_code)
        vorige_gokken.append((gok, zwartepen, wittepen))
        feedback = zwartepen, wittepen
        #Als de feedback 0 is dan wordt de gok van de lijst
        if feedback == (0,0) :
            for i in range(len(Aantal_Moelijkhede())):
                if gok == Aantal_Moelijkhede()[i]:
                    Aantal_Moelijkhede().remove(gok)
        print(gok, "|", zwartepen, "| ", wittepen)
        if zwartepen == 4:
            # Break ! we hebben de gehaime code gevonden !
            break
        pogingen = pogingen + 1
        while True:
            # genereer een nieuwe willekeurige gok, consistent met
            # alle eerdere gokken !.
            gok = Geef_een_Gok(gok)
            consistent = True
            for g, zwartepen, wittepen in vorige_gokken:
                nz, nw = evaluate(gok, g)
                if nz != zwartepen or nw != wittepen:
                    consistent = False
                    break
            if consistent:
                break
    print("==========================")
    return gok, pogingen



def Game():
    global kleur_code
    spelen = True
    kleur_code = randomcode()

    print(" --- MASTERMIND --- \n")
    print(" Welke Algorithem Wilt u het Zien ? \n")
    print("1. Simpel \n 2. Worst Case \n 3. Eigen \n")
    print("Raad de geheime kleurcode in zo min mogelijk pogingen.\n")
    print("Voer uw kleurcode in. \n U kunt rood (A), groen (B), blauw (C), geel (D), wit (E) en roze (F) gebruiken.\n")
    print("Het Gehiheme Code is ==( ",kleur_code ,")====")

    alg = int(input("Voer hier de nummer in \n "))
    if alg == 1:
        speler_gok, pogingen = Simpel_strategy(kleur_code)

    elif alg == 2:
        speler_gok, pogingen = Worst_case_strategy(kleur_code)
    elif alg == 3:
        speler_gok, pogingen = Eigen_Strategy(kleur_code)

    while spelen:
        b, w = 0, 0
        gokeset, secretset = set([]), set([])

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
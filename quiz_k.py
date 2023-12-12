#Intro bzw Erklärung zum Quiz
print ("\n\nHallo Willkommen zum Schlaue Fragen Quiz!\nTrage einfach deine Antwort unter die Frage ein.")
print ("Auf gehts, ab gehts!")
print ("\n° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° °\n")

#Antwortmöglichkeiten
fragen = [
["Wie viele Tasten hat ein Klavier?", "74", "86", "36", "88", "D" [1,3]],
["Wie viel Oscars gewann der Film \"Titanic\"?", "5", "16", "11", "9", "C"[2,4]],
["Aus wie vielen Einzelknochen besteht eine menschliche Hand?", "76", "15", "124", "27", "D"[1,3]],
["Wie viele Inseln hat das Land Schweden?", "356", "487.995", "221.831", "27", "C"[2,4]],
]
anzahl_joker = 1
#Schleife für Neustart
antwort = "NOCHMAL"
while antwort.upper() == "NOCHMAL":

    #Fragen- und Punktesystem Ablauf
    punkte = 0
    i = 0
    while i < 4:
        anzahl_joker = 1
        antwort = input("Was ist Deine Antwort?\nOder möchtest du aufhören? Dann tippe \"Ende\"\n")
        if anzahl_joker < 1:
            print: ("Falls du dir nicht sicher bist kannst du, wenn du\"50\" tippst einen 50-50 Joker anwenden.")

    #Reaktion auf Antwort mit Punktestand und Möglichkeit Joker einzulösen oder Spiel zu beenden

joker_eingelöst = False
        if antwort.upper() == frage[5]:
            print("\nYEAHHH!Du gewinnst +1 Punkt!\nAuf zur nächsten Frage!\n")
            punkte = punkte+1

        #Wenn 50-50 Joker eingelöst wird
        elif antwort.upper() == "50":
            print("Du hast deinen 50-50 Joker eingelöst")

        if joker_eingelöst == True:
            if 1 in frage[6]:
                print("A:", frage [1] "nicht richtig")
            else:
                print ("A", frage [1])
            if 2 in frage[6]:
                print("A:", frage [2] "nicht richtig")
            else:
                print ("A", frage [2])
            if 3 in frage[6]:
                print("A:", frage [3] "nicht richtig")
            else:
                print ("A", frage [3])
            if 4 in frage[6]:
                print("A:", frage [4] "nicht richtig")
            else:
                print ("A", frage [4])
            anzahl_joker = anzahl_joker -1
            joker_eingelöst = False
        elif:
        print(frage[0])
        print("A:", frage[1])
        print("B:", frage[2])
        print("C:", frage[3])
        print("D:", frage[4])


        #Wenn Spiel beendet werden soll
        elif antwort.upper() == "ENDE":
            vorigefrage = fragen[i-1]
            i = 4
        else:
            print("\nÄhm...nö.")

    if not joker_eingelöst:
        i = i+1

        print ("Dein Punktestand:",punkte,"\n")

    #Ende und Möglichkeit zu wiederholen
    print ("Das wars, gut gemacht! \nDu hast insgesamt:",punkte,"Punkt(e) gesammelt, super!\n")
    antwort = input ("Möchtest du nochmal spielen? \nDann schreibe \"Nochmal\",falls nicht, schreibe \"Beenden\"\n")

    if antwort.upper() == "NOCHMAL":
        print("\nSuper, los gehts!\n")

    else:
        print ("Okay, bis dann!")

#TODO:joker funktioniert noch nicht, schrift anpassen?

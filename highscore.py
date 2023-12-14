print("Was ist Dein Benutzername?")
name = input()
print("Dein Name ist", name)

# Anfang: Highscore noch unbekannt.
highscore_datei = "highscore.txt"
highscore_name = "Niemand"
highscore_punkte = "0"

while True:

    # Highscores werden aus Datei gelesen.
    try:
        datei = open(highscore_datei, "r")
        highscore_name = datei.readline().strip()
        highscore_punkte = datei.readline().strip()
        datei.close()
        print("Der Highscore ist", highscore_punkte, "von", highscore_name)
        print("Mal sehen, ob Du das toppen kannst!")
    except:
        print("Es gibt noch keinen Highscore.")

    print("Simulation vom Spiel... Du erreicht wie viele Punkte?")
    punkte = input()

    if int(punkte) >= int(highscore_punkte):
        print("Du hast den Highscore geknackt!")
        print(name, file=open(highscore_datei, "w"))
        print(punkte, file=open(highscore_datei, "a"))
    else:
        print("Du hast weniger als den Highscore. Du hast es leider nicht auf die Liste geschafft.")
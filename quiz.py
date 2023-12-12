###########################################################################################################
# (a) Quiz im Stil von „Wer wird Millionär“
###########################################################################################################
#                         Autor: Juliane Wahrenberg
#
# (b) Dem Benutzer werden der Reihe nach Fragen mit vier möglichen Antworten
#     präsentiert.
# (c) Aus diesen kann er wählen, indem er die entsprechende Taste (a, b, c oder
#     d) benutzt.
# (d) Der Benutzer kann einmal in der Runde ein 50/50 Joker anwenden undn das Spiel vorzeitig beenden
# (e) Der Benutzer kann mit richtigen Antworten Punkte erreichen und das Spiel vorzeitig beenden
#
###########################################################################################################

# *** Anfang des Programms ***

# Begrüßung (a)
print("\nWie soll ich Dich nennen?")
name = input()

print("\nLang ist es her und jetzt ist es endlich wieder soweit:\nHerzlich willkommen", name, "zu einer neuen Ausgabe von Wer wird Millionär!\nDas heutige Thema lautet: \"Quer durch Afrika\"\nEs geht direkt los!\n")

# Liste an Fragen (b)
fragen = [
#  ["Frage", "Antwort A", "Antwort B", "Antwort C", "Antwort D", "Richtige Antwort", Punkte, [Antworten, um bei Joker zu streichen]]
   ["Wie viele Giraffen leben in Afrika?", "2.500", "68.000", "15.000", "79.000", "B", "50", [1,3]],
   ["Wie viele Tage hat ein SchaltJahr in Afrika?", "364", "510", "365", "366", "D", "100", [1,3]],
   ["Auf welchem Komntinent liegt Timbuktu?", "Asien", "Australien", "Deutschland", "Afrika", "D", "200", [1,3]],
   ["In welchem afrikanischen Land kann man die meißten Pyramiden bewundern?", "Elfenbeinküste", "Ägypten", "Marokko", "Sudan", "D", "300", [1,3]],
   ["Welche Sprache wird in Südafrika hauptsächlich gesprochen?", "Französisch", "Spanisch", "Englisch","Östereichisch", "C", "500", [1,3]],
   ["Die Ägyptischen Pyramiden sind nicht nur sehr bekannt, sondern auch sehr groß.\nWie viele Elefanten ist die größte Pyramide, die cheops Pyramide, hoch?", "50", "105", "43", "19", "C", "1000", [1,4]],
   ["Welche Tierart ist untypisch für die afrikanische Savanne?", "Nilpferde", "Nashörner", "Pinguine", "Strauße", "C", "2000", [1,2]],
   ["Wie viele Läner liegen auf dem Kontinent Afrika?", "54", "88", "5", "33", "A", "4000", [2,3]],
   ["Welcher Ozean liegt im Westen von Afrika", "Indische Ozean", "Atlanitsche Ozean", "Mittelmeer", "pazifische Ozean", "B", "8000", [1,3]],
   ["Wie heißt der längste Fluss in Afrika?", "Niger", "Kongo", "Rhein", "Nil", "D", "16000", [1,3]],
   ["Wie viel größer ist Europa als Afrika?", "doppelt so groß", "fünf mal so groß", "sieben mal so groß", "dreimal so groß", "D", "32000", [1,3]],
   ["In welchem afrikanischen Land fand 2010 die Fußballweltmeisterschaft statt?", "Südafrika", "Niger", "Elfenbeinküste", "Ägypten", "A", "64000", [2,4]],
   ["Wie viel Kilogramm Fleisch isst ein Löwe durchschnittlich im Monat? ", "50", "120", "210", "300", "C", "125000", [1,4]],
   ["Welches Land liegt nich auf dem afrikanischen Kontinent?", "Kenia", "Indien", "Östereich", "Argentinien", "A", "500000", [3,4]],
   ["wie viel Stunden Zeitdifferenz herrscht zwischen Südafrika und Deutschland während der deutschen Winterzeit", "10", "0", "6", "3", "B", "1000000", [1,4]],
]


# Beginn der Schleife über die Spiele
antwort = "JA"
while antwort.upper() == "JA":

   punkte = 0
   anzahl_joker = 1
   joker_ist_aktiv = False

   # Versuchen, den aktuellen Highscore zu lesen
   highscore_datei = "highscore.txt"
   highscore_name = "Niemand"
   highscore_punkte = "0"

   try:
      datei = open(highscore_datei, "r")
      highscore_name = datei.readline().strip()
      highscore_punkte = datei.readline().strip()
      datei.close()
      print("Der Highscore ist", highscore_punkte, "von", highscore_name)
      print("Mal sehen, ob Du das toppen kannst!\n")
   except:
      print("Aktuell gibt es noch keinen Highscore.\n")

   # Beginn der Schleife über die Fragen in einem Spiel
   i = 0
   while i < 15:
      frage = fragen[i]
      # Präsentation der Frage (b)
        # Joker angewendet (d)

      if not joker_ist_aktiv:
         print("Mit der folgenden Frage erreichst Du", frage[6], "Punkte:")
         print(frage[0])
         print("A:", frage[1])
         print("B:", frage[2])
         print("C:", frage[3])
         print("D:", frage[4])
      else:
         print("Folgende Fragen bleiben übrig:")
         if not 1 in frage[7]:
             print("A:", frage[1])
         if not 2 in frage[7]:
             print("B:", frage[2])
         if not 3 in frage[7]:
             print("C:", frage[3])
         if not 4 in frage[7]:
             print("D:", frage[4])
         # Joker nicht angewendet (d)
         joker_ist_aktiv = False



# Fragen nach Antwort (c,d)
      if anzahl_joker > 0:
         gueltige_antworten = ["A", "B", "C", "D", "JOKER", "ENDE"]
      else:
         gueltige_antworten = ["A", "B", "C", "D", "ENDE"]
      antwort = ""
      while not antwort.upper() in gueltige_antworten:
         if i == 0:
            print("Was ist deine Antwort?")
         else:
            print("Was denkst du dieses Mal?\nDu kannst auch deine bis jetzt erreichten Punkte mit nach hause und beende das Spiel mit \"Ende\" beenden.")
         if anzahl_joker > 0:
            print("Du kannst auch mit \"Joker\" auch Deinen 50:50 Joker einlösen.\nAber denk dran: Du hast nur einen in der gesamten Runde.\n")
         antwort = input()
         if not antwort.upper() in gueltige_antworten:
            print("Das habe ich nicht verstanden. Bitte gib' a, b, c, d Ende ein!")
            if anzahl_joker > 0:
               print("Oder Joker.")

# Reaktion auf Antwort (e)
      if antwort.upper() == frage[5]:
         print("Perfekt! Du hast jetzt", (frage[6]), "Punkte.\n")
      elif antwort.upper() == "JOKER":
         print("Ok, Du hast Deinen 50:50 Joker eingesetzt.")
         anzahl_joker = anzahl_joker - 1
         joker_ist_aktiv = True
      elif antwort.upper() == "ENDE":
         if i > 0:
            vorigefrage = fragen[i-1]
            punkte = vorigefrage[6]
         print("Ok, dann gehst du mit", punkte, "Punkten nach Hause.")
         i = 15
      else:
         print("Das stimmt so nicht! Du bist raus und deine Punkte weg.")
         i = 15

      if not joker_ist_aktiv:
         i = i + 1

   # Schauen, ob es neuen Highscore gibt:
   if int(punkte) >= int(highscore_punkte):
      print("Du hast den Highscore geknackt!")
      print(name, file=open(highscore_datei, "w"))
      print(punkte, file=open(highscore_datei, "a"))
   else:
      print("Du hast weniger als den Highscore. Du hast es leider nicht auf die Liste geschafft.")

# Nochmal spielen?
   antwort = input("Willst du noch eine Runde spielen? Dann tippe \"JA\", ansonsten etwas anderes.")
   if antwort.upper() == "JA":
      print("Auf gehts zur nächsten Runde!")

print("Na dann auf Wiedersehen")

import random, time

gesamtpunkte = 0

while gesamtpunkte < 10:

   rechenzeichen = random.choice(["+", "-", "*", "/"])

   if rechenzeichen == "+":

      zahl1 = random.randint(0, 100)
      zahl2 = random.randint(0, 100 - zahl1)

      ergebnis = zahl1 + zahl2

   if rechenzeichen == "-":
      zahl1 = random.randint(0, 100)
      zahl2 = random.randint(0, zahl1)
      ergebnis = zahl1 - zahl2

   if rechenzeichen == "*":
      zahl1 = random.randint(1, 2)
      zahl2 = random.randint(1, 100 // zahl1)
      ergebnis = zahl1 * zahl2

   if rechenzeichen == "/":
      zahl1 = random.randint(1, 100)
      zahl2 = random.randint(1, 100 // zahl1)
      ergebnis = zahl1
      zahl1 = zahl1 * zahl2 

startzeit = time.time()
antwort_str = input(str(zahl1) + " " + rechenzeichen + " " + str(zahl2) + "?")
endzeit = time.time()
dauer = endzeit - startzeit
antwort = int(antwort_str)

if ergebnis == antwort:
   print("Richtig, du hast" + str(round(dauer, 1)) + "Sekunden gebraucht!")
else:
   print("Falsch! Die richtige antwort wäre" + str(ergebnis) + "gewesen.") 

   if ergebnis == antwort:
      if dauer <= 3:
         punkte = 3
      elif dauer <=5:
         punkte = 2
      else:
         punkte = 1
      gesamtpunkte += punkte
      print("Richtig, du hast" + str(round(dauer, 1)) + "Sekunden gebraucht! Hierfür erhälst du " + str(punkte) + (" punkte" if punkte > 1 else "Punkt.")+ "in") 
   else:
         print("Falsch! Die richtige antwort wäre" + str(ergebnis) + "gewesen.") 


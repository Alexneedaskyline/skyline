
import random
from Wörterliste import wörterbuch
from colored import stylize, fg 

print("Herzlich willkommen bei Wordle!")

antwort = input("Möchtest du die Anleitung sehen?")

if antwort == "ja" or antwort == "ja":
    print("finde das Wort! Es hat fünf Buchstaben. Wenn ein eingegebener Buchstabe so richtig ist, wird er grün. Wenn er zumindest im Wort vorkommt, "\
        + "aber an einer anderen Stelle, dann wird er gelb. Du hast sechs versuche - viel Erfolg!")

wort = random.choice(wörterbuch)
eingabe = ""
versuch = 0

while eingabe != wort and versuch < 6:
    
    versuch = versuch + 1


    eingabe = input("Versuch" + str(versuch) + ": Welches Wort möchtest du eingeben? ")
    
    ausgabe =""
    for i in range(5):
    
        if eingabe[i] == wort[i]:
                ausgabe = ausgabe + stylize(eingabe[i], fg(2))
        else:
            for j in range(5):
                if eingabe[i] == wort[j]:
                    ausgabe = ausgabe + stylize(eingabe[i], fg(11))
                break
            else:
                   ausgabe = ausgabe + stylize(eingabe[i], fg(255))

print(ausgabe)
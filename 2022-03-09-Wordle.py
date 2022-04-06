import random
from urllib.request import AbstractBasicAuthHandler
from colored import stylize, fg 

print("Herzlich willkommen bei Wordle!")

antwort = input("Möchtest du die Anleitung sehen?")

if antwort == "ja" or antwort == "ja":
    print("finde das Wort! Es hat fünf Buchstaben. Wenn ein eingegebener Buchstabe so richtig ist, wird er grün. Wenn er zumindest im Wort vorkommt, "\
        + "aber an einer anderen Stelle, dann wird er gelb. Du hast sechs versuche - viel Erfolg!")

wörterbuch = ["APFEL", "BIRNE", "KATZE", "TIGER", "WOLKE", "SONNE", "MILCH", "RECHT", "GLEIS", "BARKE", "SUMME", "PFERD", "MUSIK", "LICHT", "ROLLE",\
    "TISCH", "REGAL", "GRIES", "BUSCH", "OSTEN"]

wort = random.choice(wörterbuch)
eingabe = ""
versuch = 0

while eingabe != wort and versuch < 6:
    
    versuch = versuch + 1


    eingabe = input("Versuch" + str(versuch) + ": Welches Wort möchtest du eingeben? ")

    farben = ["grau", "grau", "grau", "grau", "grau"]


    if eingabe[0] == wort[0]:
        farben[0] = "grün"
    elif eingabe[0] == wort[1] or eingabe[0] == wort[2] or eingabe[0] == wort[4] or eingabe[0] == wort[4]: 
        farben[0]= "gelb"

    if eingabe[1] == wort[1]:
        farben[1] = "grün"
    elif eingabe[1] == wort[2] or eingabe[1] == wort[2] or eingabe[1] == wort[3] or eingabe[1] == wort[4]: 
        farben[1]= "gelb"

    if eingabe[2] == wort[2]:
        farben[2] = "grün"
    elif eingabe[2] == wort[2] or eingabe[2] == wort[1] or eingabe[2] == wort[3] or eingabe[2] == wort[4]: 
        farben[2]= "gelb"

    if eingabe[3] == wort[3]:
        farben[3] = "grün"
    elif eingabe[3] == wort[2] or eingabe[3] == wort[1] or eingabe[3] == wort[2] or eingabe[3] == wort[4]: 
        farben[3]= "gelb"

    if eingabe[4] == wort[4]:
        farben[4] == "grün"
    elif eingabe[4] == wort[2] or eingabe[4] == wort[1] or eingabe[4] == wort[2] or eingabe[4] == wort[3]: 
        farben[4]= "gelb"

    ausgabe = ""

    if farben[0] =="grün":
        ausgabe = ausgabe + stylize(eingabe[0], fg(2))
    elif farben[0]  == "gelb":
        ausgabe = ausgabe + stylize(eingabe[0], fg(11))
    else:
        ausgabe = ausgabe + stylize(eingabe[0], fg(255)) 

    if farben[1] =="grün":
        ausgabe = ausgabe + stylize(eingabe[1], fg(2))
    elif farben[1]  == "gelb":
        ausgabe = ausgabe + stylize(eingabe[1], fg(11))
    else:
        ausgabe = ausgabe + stylize(eingabe[1], fg(255)) 

    if farben[2] =="grün":
        ausgabe = ausgabe + stylize(eingabe[2], fg(2))
    elif farben[2]  == "gelb":
        ausgabe = ausgabe + stylize(eingabe[2], fg(11))
    else:
        ausgabe = ausgabe + stylize(eingabe[2], fg(255)) 
    
    if farben[3] == "grün":
        ausgabe = ausgabe + stylize(eingabe[3], fg(2))
    elif farben[3]  == "gelb":
        ausgabe = ausgabe + stylize(eingabe[3], fg(11))
    else:
        ausgabe == ausgabe + stylize(eingabe[3], fg(255))  

    if farben[4] == "grün":
        ausgabe = ausgabe + stylize(eingabe[4], fg(2))
    elif farben[4]  == "gelb":
        ausgabe == ausgabe + stylize(eingabe[4], fg(11))
    else:
        ausgabe = ausgabe + stylize(eingabe[4], fg(255)) 

    print(ausgabe)

    durchlauf = durchlauf - 1 

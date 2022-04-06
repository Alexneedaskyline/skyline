import random

# Begrüßung
print("Hallo lieber Spieler, willkommen zu Hangman!")

hangman_liste = ["_|_ .. .",\
    " |\n |\n_|_ .. .",\
    " |\n |\n |\n |\n_|_.. .",\
    " __\n |\n |\n |\n |\n |\n_|_.. .",\
    " ____\n |\n |\n |\n |\n |\n_|_.. .",\
    " _____\n |   |\n |\n |\n |\n |\n_|_.. .",\
    " _____\n |   |\n |   o\n |\n |\n |\n_|_.. .",\
    " _____\n |   |\n |   o\n |  -|\n |\n |\n_|_.. .",
    " _____\n |   |\n |   o\n |  -|-\n |\n |\n_|_.. .",
    " _____\n |   |\n |   o\n |  -|-\n |  /\n |\n_|_.. .",
    " _____\n |   |\n |   o\n |  -|-\n |  / \ \n |\n_|_.. ."]

wörterbuch = []
datei = open("wörterbuch.txt")
for zeile in datei.readlines():
    wörterbuch.append(zeile[:-1])

# Geheimes Wort festlegen
wort = random.choice(wörterbuch)
verdeckt = "_ " * len(wort)

runde = 0
richtige = 0
while runde < 11:
    # Spieler nach Buchstaben fragen
    print(verdeckt)
    eingabe = input("Wähle einen Buchstaben: ")

    # Auswertung
    treffer = False
    i = 0
    while i < len(wort):
    
        if wort[i].lower() == eingabe.lower() and verdeckt[i*2] == "_":
            verdeckt = verdeckt[:i*2] + wort[i] + verdeckt[i*2 + 1:]
            treffer = True
            richtige = richtige + 1
        i = i + 1
    
    if richtige == len(wort):
        print("Herzlichen Glückwunsch, du hast das Wort gefunden!")
        break

    if treffer == False:
        runde = runde + 1

    print("\n" + hangman_liste[runde - 1])

    if runde == 10:
        print("Das richtige Wort wäre gewesen: " + str(wort))

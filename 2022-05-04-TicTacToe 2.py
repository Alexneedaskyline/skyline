from colored import stylize, fg
import random 


def ausgabe(spielfeld):
    print(" " + spielfeld[0][0] + " | " + spielfeld[0][1] + " | " + spielfeld[0][2])
    print("-----------")
    print(" " + spielfeld[1][0] + " | " + spielfeld[1][1] + " | " + spielfeld[1][2])
    print("-----------")
    print(" " + spielfeld[2][0] + " | " + spielfeld[2][1] + " | " + spielfeld[2][2])


def spielerzug(spielfeld):
    eingabe_gültig = False 
    while eingabe_gültig == False:
        feld = input("Welches Feld wollen Sie wählen? ")
        if feld in ["1","2","3","4","5","6","7","8","9"] and spielfeld[(int(feld) - 1) // 3][(int(feld) - 1) % 3] in ["1","2","3","4","5","6","7","8","9"]:
            eingabe_gültig = True 
        else:
            print("Ungültige Eingabe")
    return feld


def gewinnprüfung(spielfeld):
    if (spielfeld[0][0] == spielfeld[0][1] == spielfeld[0][2]) or \
        (spielfeld[1][0] == spielfeld[1][1] == spielfeld[1][2] ) or \
            (spielfeld[2][0] == spielfeld[2][1] == spielfeld[2][2]) or \
                (spielfeld[0][0] == spielfeld[1][0] == spielfeld[2][0]) or \
                    (spielfeld[0][1] == spielfeld[1][1] == spielfeld[2][1]) or \
                        (spielfeld[0][2] == spielfeld[1][2] == spielfeld[2][2]) or \
                            (spielfeld[0][0] ==  spielfeld[1][1] == spielfeld[2][2]  ) or \
                                (spielfeld[0][2] == spielfeld[1][1] == spielfeld[2][0]):
        return True 
    else:
        return False

def computerzug(spielfeld):
    feld = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
    print("Der Computer wählt Feld " + feld)
    return feld 





print("Hallo Spieler, willkommen bei Tic Tac Toe!")

# Spielfeld anlegen
spielfeld = [["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"]]

ausgabe(spielfeld)

spieler = "x"

spiel_vorbei = False

while spiel_vorbei == False:
    if spieler == "x":
        feld = spielerzug(spielfeld)
    else:
        feld = computerzug(spielfeld)

    

    spielfeld[(int(feld) - 1) // 3][(int(feld) - 1) % 3] = stylize (spieler, fg(1 if spieler  == "x" else 31))

    ausgabe (spielfeld)


    if gewinnprüfung(spielfeld) == True:
            print("Glückwunsch Spieler " + spieler + ", du hast gewonnen!")
            spiel_vorbei = True

    if spielfeld[0][0] != "1" and spielfeld[0][1] != "2" and spielfeld[0][2] != "3" and spielfeld[1][0] != "4" and spielfeld[1][1] != "5" and spielfeld[1][2] != "6" and spielfeld[2][0] != "7" and spielfeld[2][1] != "8" and spielfeld[2][2] != "9":
            print("unentschieden...Leider  :)")
            spiel_vorbei = True
    # Spieler wechseln
    if spieler == "x":
        spieler = "o"
    else:
        spieler = "x"
    




        
        



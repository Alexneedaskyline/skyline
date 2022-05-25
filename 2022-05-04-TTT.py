from colored import stylize, fg
print("Hallo Spieler, willkommen bei Tic Tac Toe!")

# Spielfeld anlegen
spielfeld = [["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"]]

# Spielfeld ausgeben
print(" " + spielfeld[0][0] + " | " + spielfeld[0][1] + " | " + spielfeld[0][2])
print("-----------")
print(" " + spielfeld[1][0] + " | " + spielfeld[1][1] + " | " + spielfeld[1][2])
print("-----------")
print(" " + spielfeld[2][0] + " | " + spielfeld[2][1] + " | " + spielfeld[2][2])

spieler = "x"
runde = 0
spiel_vorbei = False

while spiel_vorbei == False or runde != 9:
    

    # Spieler nach seinem Zug fragen
    

    eingabe_gültig = False
    while eingabe_gültig == False:
        feld = input("Welches Feld wollen Sie wählen? ")
        if feld in ["1","2","3","4","5","6","7","8","9"] and spielfeld[(int(feld) - 1) // 3][(int(feld) - 1) % 3] in ["1","2","3","4","5","6","7","8","9"]:  
            eingabe_gültig = True
        else:
            print("Üngultige Eingabe")
    
    
    
    # Zug durchführen
    spielfeld[(int(feld) - 1) // 3][(int(feld) - 1) % 3] = stylize(spieler, fg(1 if spieler == "x" else 31))

    # Spielfeld ausgeben
    print(" " + spielfeld[0][0] + " | " + spielfeld[0][1] + " | " + spielfeld[0][2])
    print("-----------")
    print(" " + spielfeld[1][0] + " | " + spielfeld[1][1] + " | " + spielfeld[1][2])
    print("-----------")
    print(" " + spielfeld[2][0] + " | " + spielfeld[2][1] + " | " + spielfeld[2][2])

    # Prüfen, ob Spieler gewonnen hat
    if (spielfeld[0][0] == spieler and spielfeld[0][1] == spieler and spielfeld[0][2] == spieler) or \
        (spielfeld[1][0] == spieler and spielfeld[1][1] == spieler and spielfeld[1][2] == spieler) or \
            (spielfeld[2][0] == spieler and spielfeld[2][1] == spieler and spielfeld[2][2] == spieler) or \
                (spielfeld[0][0] == spieler and spielfeld[1][0] == spieler and spielfeld[2][0] == spieler) or \
                    (spielfeld[0][1] == spieler and spielfeld[1][1] == spieler and spielfeld[2][1] == spieler) or \
                        (spielfeld[0][2] == spieler and spielfeld[1][2] == spieler and spielfeld[2][2] == spieler) or \
                            (spielfeld[0][0] == spieler and spielfeld[1][1] == spieler and spielfeld[2][2] == spieler) or \
                                (spielfeld[0][2] == spieler and spielfeld[1][1] == spieler and spielfeld[2][0] == spieler):
        print("Glückwunsch Spieler " + spieler + ", du hast gewonnen!")
        spiel_vorbei = True

    if spielfeld[0][0] != "1" and spielfeld[0][1] != "2" and spielfeld[0][2] != "3" and spielfeld[1][0] != "4" and spielfeld[1][1]!= "5"\
        and spielfeld[1][2] != "6" and spielfeld[2][0] != "7" and spielfeld[2][1] != "8" and spielfeld[2][2] != "9":
       print(unentschieden...Leider) 
        spiel_vorbei = True 

    # Spieler wechseln
    if spieler == "x":
        spieler = "o"
    else:
        spieler = "x"
    
    runde = runde + 1

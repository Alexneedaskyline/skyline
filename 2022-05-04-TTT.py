from colored import stylize, fg

print("Hallo Spieler, willkommen bei Tic Tac Toe!")

# Spielfeld anlegen
spielfeld = [["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"]]

# Spielfeld ausgeben
def print_spielfeld():
    print(" " + spielfeld[0][0] + " | " + spielfeld[0][1] + " | " + spielfeld[0][2])
    print("-----------")
    print(" " + spielfeld[1][0] + " | " + spielfeld[1][1] + " | " + spielfeld[1][2])
    print("-----------")
    print(" " + spielfeld[2][0] + " | " + spielfeld[2][1] + " | " + spielfeld[2][2])

spieler = "x"
runde = 0
spiel_vorbei = False

while not spiel_vorbei and runde != 9:
    # Spielfeld ausgeben
    print_spielfeld()

    # Spieler nach seinem Zug fragen
    eingabe_gültig = False
    while not eingabe_gültig:
        feld = input("Welches Feld wollen Sie wählen? ")
        if feld in ["1","2","3","4","5","6","7","8","9"] and spielfeld[(int(feld) - 1) // 3][(int(feld) - 1) % 3] in ["1","2","3","4","5","6","7","8","9"]:
            eingabe_gültig = True
        else:
            print("Ungültige Eingabe")

    # Zug durchführen
    spielfeld[(int(feld) - 1) // 3][(int(feld) - 1) % 3] = stylize(spieler, fg(1 if spieler == "x" else 31))

    # Prüfen, ob Spieler gewonnen hat
    for i in range(3):
        if (spielfeld[i][0] == spieler and spielfeld[i][1] == spieler and spielfeld[i][2] == spieler) or \
            (spielfeld[0][i] == spieler and spielfeld[1][i] == spieler and spielfeld[2][i] == spieler):
            print("Glückwunsch Spieler " + spieler + ", du hast gewonnen!")
            spiel_vorbei = True

    # Prüfen, ob unentschieden
    if all(cell not in ["1","2","3","4","5","6","7","8","9"] for row in spielfeld for cell in row):
        print("Unentschieden...Leider!")
        spiel_vorbei = True

    # Spieler wechseln
    spieler = "o" if spieler == "x" else "x"
    runde += 1

# Spielfeld am Ende noch einmal ausgeben
print_spielfeld()

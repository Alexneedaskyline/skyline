print("Hallo Spieler, willkommen bei Tic Tac Toe")

spielfeld = [["1", "2", "3"],
             ["4", "5", "6"],
             ["7", "8", "9"]]




print(" " + spielfeld[0][0] + " | " + spielfeld[0][1] + " | " + spielfeld[0][2])
print("-----------")
print(" " + spielfeld[1][0] + " | " + spielfeld[1][1] + " | " + spielfeld[1][2])
print("-----------")
print(" " + spielfeld[2][0] + " | " + spielfeld[2][1] + " | " + spielfeld[2][2])
print("-----------")
spieler = "x"

spiel_vorbei = False
while spiel_vorbei == False: 

    
    feld = input("Welches Feld wollen Sie wählen?")



    spielfeld[(int(feld) - 1) // 3][(feld -1) % 3] = "x"

    print(" " + spielfeld[0][0] + " | " + spielfeld[0][1] + " | " + spielfeld[0][2])
    print("-----------")
    print(" " + spielfeld[1][0] + " | " + spielfeld[1][1] + " | " + spielfeld[1][2])
    print("-----------")
    print(" " + spielfeld[2][0] + " | " + spielfeld[2][1] + " | " + spielfeld[2][2])
    print("-----------")

if  (spielfeld[0][0] == spieler and spielfeld[0][1] == spieler and spielfeld[0][2] == spieler) or \ 
    (spielfeld[1][0] == spieler and spielfeld[1][1] == spieler and spielfeld[1][2] == spieler) or \ 
    (spielfeld[2][0] == spieler and spielfeld[2][1] == spieler and spielfeld[2][2] == spieler) or \ 
    (spielfeld[0][0] == spieler and spielfeld[1][0] == spieler and spielfeld[2][0] == spieler) or \ 
    (spielfeld[0][1] == spieler and spielfeld[1][1] == spieler and spielfeld[2][1] == spieler) or \ 
    (spielfeld[0][2] == spieler and spielfeld[1][2] == spieler and spielfeld[2][2] == spieler) or \ 
    (spielfeld[0][0] == spieler and spielfeld[1][1] == spieler and spielfeld[2][2] == spieler) or \ 
    (spielfeld[0][2] == spieler and spielfeld[1][1] == spieler and spielfeld[2][0] == spieler) or \ :
    
    print("Glückwunsch " + spieler + ", du hast gewonnen! ")
    spiel_vorbei = Trueb
    if spieler == "x":
        spieler = "o"
    else:
        spieler = "x"
import arcade, random
import arcade.color

class TTT(arcade.Window):
    def __init__(self):
        super().__init__(600, 600, "Tic Tac Toe")

        self.spielfeld = {(0, 0): "", (1, 0): "", (2, 0): "", (0, 1): "", (1, 1): "", (2, 1): "", (0, 2): "", (1, 2): "", (2, 2): ""}
        self.spieler = "X"

    def gewinnprüfung(self):
        if self.spielfeld [(0, 0)] == self.spielfeld[(1, 0)] == self.spielfeld[(2, 0)] !="": 
            return True
        if self.spielfeld [(0, 1)] == self.spielfeld[(1, 1)] == self.spielfeld[(2, 1)] !="":
            return True
        if self.spielfeld [(0, 2)] == self.spielfeld[(1, 2)] == self.spielfeld[(2, 2)] !="":
            return True
        if self.spielfeld [(0, 0)] == self.spielfeld[(0, 1)] == self.spielfeld[(0, 2)] !="":
            return True
        if self.spielfeld [(1, 0)] == self.spielfeld[(1, 1)] == self.spielfeld[(1, 2)] !="":
            return True
        if self.spielfeld [(2, 0)] == self.spielfeld[(2, 1)] == self.spielfeld[(2, 2)] !="":
            return True
        if self.spielfeld [(0, 0)] == self.spielfeld[(1, 1)] == self.spielfeld[(2, 2)] !="":
            return True
        if self.spielfeld [(2, 0)] == self.spielfeld[(1, 1)] == self.spielfeld[(0, 2)] !="":
            return True
        return False
    

    def freie_felder(self):
        felder_liste = []
        for i in range(3):
            for j in range(3):
                if self.spielfeld[(i, j)] == "":
                    felder_liste.append((i, j))
        return felder_liste


    def unentschieden(self):
        if len(self.freie_felder()) == 0 and self.gewinnprüfung() == False:
            return True
        else:
            return False


        

        
    def on_mouse_press(self, x, y, button, modifiers):
        if self.spieler == "X":
            if 0 <= x < 200:
                x_spielfeld = 0
            if 0 <= y < 200:
                y_spielfeld = 0
            if 200 <= x < 400:
                x_spielfeld = 1
            if 200 <= y < 400:
                y_spielfeld = 1
            if 400 <= x < 600:
                x_spielfeld = 2
            if 400 <= y < 600:
                y_spielfeld = 2
            if self.spielfeld[(x_spielfeld, y_spielfeld)] == "" and self.gewinnprüfung() == False:
                self.spielfeld[(x_spielfeld, y_spielfeld)] = self.spieler
                if self.spieler == "X":
                    self.spieler = "O"
                else:
                    self.spieler = "X"

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.R:
            self.__init__()
        elif symbol == arcade.key.Q:
            arcade.close_window()


    def random_zug(self):
        freie_felder_liste = self.freie_felder()
        return random.choice(freie_felder_liste)

    def mittelschlauer_zug(self):
        freie_felder_liste = self.freie_felder()

        for feld in freie_felder_liste:
            self.spielfeld[feld] = "O"
            if self.gewinnprüfung() == True:
                self.spielfeld[feld] = ""
                return feld 
            self.spielfeld[feld] = "" 

        for feld in freie_felder_liste:
            self.spielfeld[feld] = "X"
            if self.gewinnprüfung() == True:
                self.spielfeld[feld] = ""
                return feld
            self.spielfeld[feld] = ""  

        return self.random_zug()
    
    def schlauer_zug(self):
        gegner_symbole = "X" if self.spieler == "O" else "X"

        freie_felder_liste = self.freie_felder()

        for feld in freie_felder_liste:
            self.spielfeld[feld] = "O"
            if self.gewinnprüfung() == True:
                self.spielfeld[feld] = ""
                return feld
            self.spielfeld[feld] = ""

        for feld in freie_felder_liste:
            self.spielfeld[feld] = "X"
            if self.gewinnprüfung() == True:
                self.spielfeld[feld] = ""
                return feld
            self.spielfeld[feld] = ""

        if len(freie_felder_liste) == 9:
            return (1, 1)
        elif len(freie_felder_liste) == 8 and self.spielfeld[(1, 1)] == gegner_symbole:
            return (2, 2)
        
        for feld in freie_felder_liste:
            self.spielfeld[feld] = gegner_symbole
            if self.gewinnprüfung() == True:
                self.spielfeld[feld] = ""
                return feld
            self.spielfeld[feld] = ""

        return self.random_zug()
    

    def on_update(self, delta_time):
        if self.spieler == "O" and not self.gewinnprüfung() and not len(self.freie_felder()) == 0:
            feld = self.mittelschlauer_zug()
            self.spielfeld[feld] = "O"
            self.spieler = "X"

    def on_draw(self):
        self.clear()

        arcade.draw_line(20, 200, 600, 200, arcade.color.WHITE, 12)
        arcade.draw_line(20, 400, 600, 400, arcade.color.WHITE, 12)
        arcade.draw_line(200, 20, 200, 600, arcade.color.WHITE, 12)
        arcade.draw_line(400,20, 400, 600, arcade.color.WHITE, 12)

        print(self.spielfeld)
        for koordinaten in self.spielfeld:
            symbol = self.spielfeld[koordinaten]
            pos_x = 200 * koordinaten[0] + 100
            pos_y = 200 * koordinaten[1] + 100
            arcade.draw_text(symbol, pos_x, pos_y, font_size=100, anchor_x= "center", anchor_y= "center")

        if self.gewinnprüfung() == True:
            arcade.draw_rectangle_filled(300, 300, 600, 600, arcade.make_transparent_color (arcade.color.BLACK, 190))
            arcade.draw_text(("X" if self.spieler == "O" else "O") + " hat gewonnen!", 0, 322.275, arcade.color.AQUA, font_size=80, width=600, align="center")


        if self.unentschieden() == True:
            arcade.draw_rectangle_filled(300, 300, 600, 600, arcade.make_transparent_color (arcade.color.BLACK, 190))
            arcade.draw_text("Unentschieden", 0, 275, arcade.color.AQUA, font_size=50, width=600, align="center")
            
TTT()
arcade.run()





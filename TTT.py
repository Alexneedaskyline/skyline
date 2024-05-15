import arcade

class TTT(arcade.Window):
    def __init__(self):
        super().__init__(600, 600, "Tic Tac Toe")

        self.spielfeld = {(0, 0): "x", (1, 0): "", (2, 0): "", (0, 1): "o", (2, 1): "", (0, 2): "", (1, 2): "", (2, 2): ""}

    def on_mouse_press(self, x, y, button, modifiers):
        print(x, y)
        
    def on_draw(self):
        self.clear()

        arcade.draw_line(20, 200, 600, 200, arcade.color.WHITE, 12)
        arcade.draw_line(20, 400, 600, 400, arcade.color.WHITE, 12)
        arcade.draw_line(200, 20, 200, 600, arcade.color.WHITE, 12)
        arcade.draw_line(400,20, 400, 600, arcade.color.WHITE, 12)

        for koordinaten in self.spielfeld:
            symbol = self.spielfeld[koordinaten]
            pos_x = 200 * koordinaten[0] + 100
            pos_y = 200 * koordinaten[1] + 100
            arcade.draw_text(symbol, pos_x, pos_y, font_size=100, anchor_x= "center", anchor_y= "center")

            
TTT()
arcade.run()


#schreibe eine funktion substring_suchstring str, substring: str) -> str, die im übergegebenen String den übergebenen sucht.
#falls substring in string enthalten ist, soll Tree zurückgegeben werden, anstonsten False. 
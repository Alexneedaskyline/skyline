import arcade

class TTT(arcade.Window):
    def __init__(self):
        super().__init__(600, 600, "Tic Tac Toe")

        spielfeld = {(0, 0:) "", (1, 0:) "", (2, 0): "", (0, 1): "", (2, 1): "", (0, 2): "", (1, 2): "", (2, 2): "")}

    def on_draw(self):
        self.clear()

        arcade.draw_line(20, 200, 600, 200, arcade.color.WHITE, 12)
        arcade.draw_line(20, 400, 600, 400, arcade.color.WHITE, 12)
        arcade.draw_line(200, 20, 200, 600, arcade.color.WHITE, 12)
        arcade.draw_line(400,20, 400, 600, arcade.color.WHITE, 12)

        for koordinaten in self.spielfeld:


TTT()
arcade.run()
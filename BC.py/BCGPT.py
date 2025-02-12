import pyglet
import arcade


SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 750

DEFAULT_LINE_HEIGHT = 45
DEFAULT_FONT_SIZE = 20


class BC(arcade.Window):
    def __init__(self):
        super().__init__(1500, 750)  # 1500 #750

        # Spieler A und B
        self.a = arcade.Sprite("a.png")
        self.a.center_x = 100
        self.a.center_y = self.height / 2
        self.a_b = 5
        self.a_lives = 3  # Leben von Spieler A

        self.b = arcade.Sprite("b.png", flipped_horizontally=True)
        self.b.center_x = self.width - 100
        self.b.center_y = self.height / 2
        self.b_b = 5
        self.b_lives = 3  # Leben von Spieler B

        # Munition
        self.munition_list = arcade.SpriteList()

        # Spielstatus
        self.game_over = False
        self.winner = None

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.Q:
            arcade.close_window()

        if self.game_over:
            if symbol == arcade.key.R:
                self.restart_game()
            return

        # Steuerung für Spieler A
        if symbol == arcade.key.W:
            self.a.change_y = self.a_b
        elif symbol == arcade.key.A:
            self.a.change_x = -self.a_b
        elif symbol == arcade.key.S:
            self.a.change_y = -self.a_b
        elif symbol == arcade.key.D:
            self.a.change_x = self.a_b

        # Steuerung für Spieler B
        if symbol == arcade.key.UP:
            self.b.change_y = self.b_b
        elif symbol == arcade.key.LEFT:
            self.b.change_x = -self.b_b
        elif symbol == arcade.key.DOWN:
            self.b.change_y = -self.b_b
        elif symbol == arcade.key.RIGHT:
            self.b.change_x = self.b_b

        # Munition abfeuern
        if symbol == arcade.key.E:
            munition = arcade.Sprite("munition1.png")
            munition.center_x = self.a.center_x
            munition.center_y = self.a.center_y
            munition.change_x = 27
            self.munition_list.append(munition)

        if symbol == arcade.key.M:
            munition = arcade.Sprite("munition2.png")
            munition.center_x = self.b.center_x
            munition.center_y = self.b.center_y
            munition.change_x = -26
            self.munition_list.append(munition)

    def restart_game(self):
        self.a.center_x = 100
        self.a.center_y = self.height / 2
        self.a.change_x = 0
        self.a.change_y = 0
        self.a_lives = 3  # Leben zurücksetzen

        self.b.center_x = self.width - 100
        self.b.center_y = self.height / 2
        self.b.change_x = 0
        self.b.change_y = 0
        self.b_lives = 3  # Leben zurücksetzen

        self.munition_list = arcade.SpriteList()
        self.game_over = False
        self.winner = None

    def update(self, delta_time):
        if self.game_over:
            return

        self.a.center_x += self.a.change_x
        self.a.center_y += self.a.change_y
        self.b.center_x += self.b.change_x
        self.b.center_y += self.b.change_y

        self.munition_list.update()

        for munition in self.munition_list:
            if munition.center_x > self.width or munition.center_x < 0:
                munition.remove_from_sprite_lists()

        for munition in self.munition_list:
            if arcade.check_for_collision(munition, self.b):
                munition.remove_from_sprite_lists()
                self.b_lives -= 1  # Leben von B verringern
                if self.b_lives <= 0:
                    self.game_over = True
                    self.winner = "A"
            elif arcade.check_for_collision(munition, self.a):
                munition.remove_from_sprite_lists()
                self.a_lives -= 1  # Leben von A verringern
                if self.a_lives <= 0:
                    self.game_over = True
                    self.winner = "B"

    def on_draw(self):
        self.clear()
        self.a.draw()
        self.b.draw()
        self.munition_list.draw()

        middle_x = self.width / 2
        arcade.draw_line(
            start_x=middle_x,
            start_y=0,
            end_x=middle_x,
            end_y=self.height,
            line_width=1,
            color=(0, 0, 0)
        )

        # Herzen für Spieler A zeichnen
        for i in range(self.a_lives):
            heart = arcade.Sprite("heart.png")  # Herz-Sprite
            heart.center_x = 50 + (i * 50)
            heart.center_y = self.height - 50
            heart.draw()

        # Herzen für Spieler B zeichnen
        for i in range(self.b_lives):
            heart = arcade.Sprite("heart.png")  # Herz-Sprite
            heart.center_x = self.width - 50 - (i * 50)
            heart.center_y = self.height - 50
            heart.draw()

        # Spieler Namen anzeigen
        arcade.draw_text("Spieler A", self.a.center_x - 750, self.a.center_y + self.a.height / 2 + 10, arcade.color.YELLOW, DEFAULT_FONT_SIZE, width=SCREEN_WIDTH, align="center")
        arcade.draw_text("Spieler B", self.b.center_x - 750, self.b.center_y + self.b.height / 2 + 10, arcade.color.BLUE, DEFAULT_FONT_SIZE, width=SCREEN_WIDTH, align="center")

        # Game Over Text
        if self.game_over:
            if self.winner == "A":
                start_x = self.width / 2 - 750
                start_y = self.height / 1.2
                arcade.draw_text("Spieler A hat gewonnen!", start_x, start_y, arcade.color.YELLOW, DEFAULT_FONT_SIZE * 2, width=SCREEN_WIDTH, align="center")
            elif self.winner == "B":
                start_x = self.width / 2 - 750
                start_y = self.height / 1.2
                arcade.draw_text("Spieler B hat gewonnen!", start_x, start_y, arcade.color.BLUE, DEFAULT_FONT_SIZE * 2, width=SCREEN_WIDTH, align="center")


if __name__ == "__main__":
    window = BC()
    arcade.run()

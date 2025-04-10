import pyglet
pyglet.options["osx_alt_loop"] = True

import arcade
import random

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 750

DEFAULT_LINE_HEIGHT = 45
DEFAULT_FONT_SIZE = 20

class BC(arcade.Window):
    def __init__(self):
        super().__init__(1500, 750)  # Set window size

        # Player A (yellow)
        self.a = arcade.Sprite("a.png")
        self.a.center_x = 100
        self.a.center_y = self.height / 2
        self.a_b = 5
        self.a_lives = 3

        # Player B (blue)
        self.b = arcade.Sprite("b.png", flipped_horizontally=True)
        self.b.center_x = self.width - 100
        self.b.center_y = self.height / 2
        self.b_b = 5
        self.b_lives = 3

        # Lists to store projectiles and energy bottles
        self.munition_list = arcade.SpriteList()
        self.energy_list = arcade.SpriteList()

        self.game_over = False
        self.winner = None

        # Generate initial energy item
        self.generate_energy()

    def generate_energy(self):
        energy = arcade.Sprite("energy.png")  
        energy.center_x = random.randint(100, self.width - 100)
        energy.center_y = random.randint(100, self.height - 100)
        self.energy_list.append(energy)

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.Q:
            arcade.close_window()

        if self.game_over:  # If game is over, allow restarting
            if symbol == arcade.key.R:
                self.restart_game()  
            return

        # Controls for Player A (yellow)
        if symbol == arcade.key.W:
            self.a.change_y = self.a_b
        elif symbol == arcade.key.A:
            self.a.change_x = -self.a_b
        elif symbol == arcade.key.S:
            self.a.change_y = -self.a_b
        elif symbol == arcade.key.D:
            self.a.change_x = self.a_b

        # Controls for Player B (blue)
        if symbol == arcade.key.UP:
            self.b.change_y = self.b_b
        elif symbol == arcade.key.LEFT:
            self.b.change_x = -self.b_b
        elif symbol == arcade.key.DOWN:
            self.b.change_y = -self.b_b
        elif symbol == arcade.key.RIGHT:
            self.b.change_x = self.b_b

        # Fire projectiles for Player A (yellow)
        if symbol == arcade.key.E:
            munition = arcade.Sprite("munition1.png")
            munition.center_x = self.a.center_x
            munition.center_y = self.a.center_y
            munition.change_x = 27
            self.munition_list.append(munition)

        # Fire projectiles for Player B (blue)
        if symbol == arcade.key.M:
            munition = arcade.Sprite("munition2.png")
            munition.center_x = self.b.center_x
            munition.center_y = self.b.center_y
            munition.change_x = -26
            self.munition_list.append(munition)

    def on_key_release(self, symbol, modifiers):
        # Stop movement when keys are released
        if symbol in (arcade.key.W, arcade.key.S):
            self.a.change_y = 0
        elif symbol in (arcade.key.A, arcade.key.D):
            self.a.change_x = 0
        elif symbol in (arcade.key.UP, arcade.key.DOWN):
            self.b.change_y = 0
        elif symbol in (arcade.key.LEFT, arcade.key.RIGHT):
            self.b.change_x = 0

    def restart_game(self):
        # Reset all game parameters
        self.a.center_x = 100
        self.a.center_y = self.height / 2
        self.a.change_x = 0
        self.a.change_y = 0
        self.a_lives = 3

        self.b.center_x = self.width - 100
        self.b.center_y = self.height / 2
        self.b.change_x = 0
        self.b.change_y = 0
        self.b_lives = 3

        self.munition_list = arcade.SpriteList()
        self.game_over = False
        self.winner = None

    def update(self, delta_time):
        if self.game_over:
            return

        # Update positions of both players
        self.a.center_x += self.a.change_x
        self.a.center_y += self.a.change_y
        self.b.center_x += self.b.change_x
        self.b.center_y += self.b.change_y
        
        self.munition_list.update()
        self.energy_list.update()

        # Handle energy bottle collection
        for energy in self.energy_list:
            if arcade.check_for_collision(self.a, energy):  
                energy.remove_from_sprite_lists()  # Remove energy bottle
                self.a_b += 2  # Increase speed for player A
                self.generate_energy()  # Generate a new energy bottle
            elif arcade.check_for_collision(self.b, energy):  
                energy.remove_from_sprite_lists()  # Remove energy bottle if player B collects it

        # Handle projectile collisions with players
        for munition in self.munition_list:
            if munition.center_x > self.width or munition.center_x < 0:
                munition.remove_from_sprite_lists()

        for munition in self.munition_list:
            if arcade.check_for_collision(munition, self.b):  
                munition.remove_from_sprite_lists()
                self.b_lives -= 1
                if self.b_lives == 0:
                    self.game_over = True
                    self.winner = "A"

            elif arcade.check_for_collision(munition, self.a):  
                munition.remove_from_sprite_lists()
                self.a_lives -= 1
                if self.a_lives == 0:
                    self.game_over = True
                    self.winner = "B"

        # Ensure players stay within screen bounds
        if self.a.left < 0:
            self.a.left = 0
        elif self.a.center_x > self.width / 2 - self.a.width / 2:
            self.a.center_x = self.width / 2 - self.a.width / 2

        if self.a.top > self.height:
            self.a.top = self.height
        elif self.a.bottom < 0:
            self.a.bottom = 0

        if self.b.right > self.width:
            self.b.right = self.width
        elif self.b.center_x < self.width / 2 + self.b.width / 2:
            self.b.center_x = self.width / 2 + self.b.width / 2

        if self.b.top > self.height:
            self.b.top = self.height
        elif self.b.bottom < 0:
            self.b.bottom = 0

    def on_draw(self):
        self.clear()

        # Draw players and projectiles
        self.a.draw()
        self.b.draw()
        self.munition_list.draw()
        self.energy_list.draw()

        # Draw dividing line between players
        middle_x = self.width / 2
        arcade.draw_line(
            start_x=middle_x,
            start_y=0,
            end_x=middle_x,
            end_y=self.height,
            line_width=1,
            color=(0, 0, 0)
        )

        # Draw health hearts for both players
        for i in range(self.a_lives):
            heart = arcade.Sprite("yellowheart.png") 
            heart.center_x = 50 + (i * 50)
            heart.center_y = self.height - 50
            heart.draw()

        for i in range(self.b_lives):
            heart = arcade.Sprite("blueheart.png")  
            heart.center_x = self.width - 50 - (i * 50)
            heart.center_y = self.height - 50
            heart.draw()

        # Draw player labels
        arcade.draw_text("Spieler A", self.a.center_x - 750, self.a.center_y + self.a.height / 2 + 10, arcade.color.YELLOW, DEFAULT_FONT_SIZE, width=SCREEN_WIDTH, align="center")
        arcade.draw_text("Spieler B", self.b.center_x - 750, self.b.center_y + self.b.height / 2 + 10, arcade.color.BLUE, DEFAULT_FONT_SIZE, width=SCREEN_WIDTH, align="center")

        # Display winner message if game is over
        if self.game_over:
            if self.winner == "A":
                start_x = self.width / 2 - 750
                start_y = self.height / 1.2
                arcade.draw_text("Spieler A hat gewonnen!",
                                 start_x,
                                 start_y,
                                 arcade.color.YELLOW,
                                 DEFAULT_FONT_SIZE * 2,
                                 width=SCREEN_WIDTH,
                                 align="center")
            elif self.winner == "B":
                start_x = self.width / 2 - 750
                start_y = self.height / 1.2
                arcade.draw_text("Spieler B hat gewonnen!",
                                 start_x,
                                 start_y,
                                 arcade.color.BLUE,
                                 DEFAULT_FONT_SIZE * 2,
                                 width=SCREEN_WIDTH,
                                 align="center")

if __name__ == "__main__":
    window = BC()
    arcade.run()

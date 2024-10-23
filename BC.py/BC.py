import pyglet
import arcade

pyglet.options["osx_alt_loop"] = True

class BC(arcade.Window):
    def __init__(self):
        super().__init__(1500, 750, "BC")
        
        self.a = arcade.Sprite("a.png")
        self.a.center_x = 100
        self.a.center_y = self.height / 2
        self.a_b = 5

        self.b = arcade.Sprite("b.png", flipped_horizontally=True)
        self.b.center_x = self.width - 100
        self.b.center_y = self.height / 2
        self.b_b = 5

        self.munition1 = arcade.Sprite("munition1.png")
        self.

        

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.W:
            self.a.change_y = self.a_b
        elif symbol == arcade.key.A:
            self.a.change_x = -self.a_b
        elif symbol == arcade.key.S:
            self.a.change_y = -self.a_b
        elif symbol == arcade.key.D:
            self.a.change_x = self.a_b

        if symbol == arcade.key.UP:
            self.b.change_y = self.b_b
        elif symbol == arcade.key.LEFT:
            self.b.change_x = -self.b_b
        elif symbol == arcade.key.DOWN:
            self.b.change_y = -self.b_b
        elif symbol == arcade.key.RIGHT:
            self.b.change_x = self.b_b

        if object == arcade.key.E:
            self.munition1.change

    def on_key_release(self, symbol, modifiers):
        if symbol in (arcade.key.W, arcade.key.S):
            self.a.change_y = 0
        elif symbol in (arcade.key.A, arcade.key.D):
            self.a.change_x = 0
        elif symbol in (arcade.key.UP, arcade.key.DOWN):
            self.b.change_y = 0
        elif symbol in (arcade.key.LEFT, arcade.key.RIGHT):
            self.b.change_x = 0

    def update(self, delta_time):

        self.a.center_x += self.a.change_x
        self.a.center_y += self.a.change_y
        self.b.center_x += self.b.change_x
        self.b.center_y += self.b.change_y


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
        self.a.draw()
        self.b.draw()

        middle_x = self.width / 2
        arcade.draw_line(
            start_x=middle_x,
            start_y=0,
            end_x=middle_x,
            end_y=self.height,
            line_width=1,
            color=(255, 0, 0)
        )


if __name__ == "__main__":
    window = BC()
    arcade.run()


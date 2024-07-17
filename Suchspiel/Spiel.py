import arcade, random


class Spiel(arcade.Window):
    def __init__(self, breite, höhe, titel):
        super().__init__(breite, höhe,titel)
        
                
                
        self.background_music = arcade.Sound("Ton.wav")

        
        arcade.set_background_color(arcade.color.BLIZZARD_BLUE)
        
        self.setup()

    def setup (self):
        self.gegenstand_liste = arcade.SpriteList()

        bigrapper = arcade.Sprite("bigrapper.png", 0.5)
        bigrapper.center_x = random.randrange(800)
        bigrapper.center_y = random.randrange(600)
        self.gegenstand_liste.append(bigrapper)

        kimjongung = arcade.Sprite("kimjongung.png", 0.5)
        kimjongung.center_x = random.randrange(800)
        kimjongung.center_y = random.randrange(600)
        self.gegenstand_liste.append(kimjongung)

        google = arcade.Sprite("google.png", 0.5)
        google.center_x = random.randrange(800)
        google.center_y = random.randrange(600)
        self.gegenstand_liste.append(google)

        bananafn = arcade.Sprite("bananafn.png", 0.5)
        bananafn.center_x = random.randrange(800)
        bananafn.center_y = random.randrange(600)
        self.gegenstand_liste.append(bananafn)

        self.hindernis_liste = arcade.SpriteList()

        for i in range(2):
            ps5pixelart = arcade.Sprite("ps5pixelart.png", 0.5)
            ps5pixelart.center_x = random.randrange(800)   
            ps5pixelart.center_y = random.randrange(600)
            self.gegenstand_liste.append(ps5pixelart)

        self.punkte = 0

        self.total_time = 0.0

        self.zahlen = 0

        self.Gewinnpunkte = 6
        
        self.gewonnen = False
        
        
        self.time_limit = 20.0
        self.time_up = False

  
  

        self.gegenstand_liste.draw()
        self.hindernis_liste.draw()

        self.background_music.play(volume=0.5, loop=True)
    
    def on_update(self, delta_time):
        if not self.gewonnen:
            self.total_time += delta_time
        
        if self.total_time >= self.time_limit:
                self.total_time = self.time_limit
                self.time_up = True

        if self.total_time >= 20.0: 
            if self.punkte < self.Gewinnpunkte:
                self.gewonnen = False
    

    def on_mouse_press(self, x, y, taste, modifiers):
        pseudosprite = arcade.Sprite()
        pseudosprite.center_x = x
        pseudosprite.center_y = y
        pseudosprite.set_hit_box([(-1, -1), (-1, 1), (1, 1), (1, -1)])

        gegenstand_hitliste = arcade.check_for_collision_with_list(pseudosprite, self.gegenstand_liste)
        for gegenstand in gegenstand_hitliste:
            gegenstand.kill()
            self.punkte += 1

        if self.punkte >= self.Gewinnpunkte:
            self.gewonnen = True
               

       
 

        
  
    def on_draw(self):
        self.clear()

        self.gegenstand_liste.draw()
        self.hindernis_liste.draw()
        start_x = 0
        start_y = 0
        arcade.draw_text(str(self.punkte), 30, 50, arcade.color.BLACK, 70)

        if self.punkte >= self.Gewinnpunkte:
            arcade.draw_text("Du hast gewonnen", 250, 300, arcade.color.BLACK, font_size=40)
        elif self.total_time >= 20.0:
            arcade.draw_text("Du hast verloren", 250, 300, arcade.color.BLACK, font_size=40)

        
        
        rounded_time = round(self.total_time, 2) 
        time_str = str(rounded_time) + "s" 
        arcade.draw_text(time_str, 750, 50, arcade.color.BLACK, 70, anchor_x="right")
           

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.Q:
            self.background_music.stop()
            arcade.close_window()
        elif symbol == arcade.key.R:
            self.setup()         

      






spiel = Spiel(800, 600, "Suchspiel")
arcade.run()







from if3_game.engine import Sprite, Layer, Text, Game
from pyglet.window import key
from math import radians, cos, sin
from random import randint


RESOLUTION = [800, 600]
CENTER = [RESOLUTION[0]/2, RESOLUTION[1]/2]


class AsteroidGame(Game):

    def __init__(self):
        super().__init__()

        self.background_layer = Layer()
        self.background_layer.add(Sprite("sprites/background.jpg"))

        self.game_layer = Layer()
        self.ship = Ship(CENTER)

        self.ui_layer = UILayer(self.ship)

        self.add(self.background_layer, self.game_layer, self.ui_layer)
        self.asteroids = []

        self.initialize()


    def initialize(self):
            
            for asteroid in self.asteroids:
                asteroid.level = 1
                asteroid.destroy()

            self.asteroids = []

            self.ship.destroy()

            self.ship = Ship(CENTER)
            self.game_layer.add(self.ship)

            self.ui_layer.ship = self.ship

            self.asteroids.append(Asteroid((100, 200), (-50, -200), 20))
            self.asteroids.append(Asteroid((750, 500), (50, 200), 20))
            
            for asteroid in self.asteroids:
                self.game_layer.add(asteroid)


class UILayer(Layer):

    def __init__(self, ship):
        super().__init__()
        # Ici, on accède aux données/variables de ship:
        self.ship = ship
        position = (10, 580)

        self.life_sprites = []
        for n in range(self.ship.hp):
            x, y = position
            # (19 parce que le coeur fait 16 pixels de long, et qu'on laisse 3 pixels entre chaque coeur)
            x += 19 * n
            life_sprite = Sprite("sprites/life.png", (x, y))
            self.add(life_sprite)
            self.life_sprites.append(life_sprite)

        # si on voulait afficher la vie via un texte:
        # self.life_text = Text(f"Life: {self.ship.hp}", (10, 530), 50)
        # il faut lui dire de mettre le texte qu'on vient de créer dans le layer, sinon on ne le verra pas.
        # self.add(self.life_text)

            self.game_over_text = Text("", CENTER, 60, anchor="center")
            self.add(self.game_over_text)


    def on_key_press(self, k, modifiers):
        if self.ship.hp <= 0 and k == key.SPACE:
            self.game.initialize()


    def update(self, dt):
        super().update(dt)

        for n in range(len(self.life_sprites)):
            if n < self.ship.hp:
                self.life_sprites[n].opacity = 255
            else:
                self.life_sprites[n].opacity = 0
        
        # Ici une façon un peu plus efficace de l'écrire
        # for n, life_sprite in enumerate(self.life_sprites):
        #     if n < self.ship.hp:
        #         life_sprite.opacity = 255
        #     else:
        #         life_sprite.opacity = 0

        # Ici la version moche
        # if self.ship.hp == 2:
        #     self.life_sprites[2].opacity = 0
        # if self.ship.hp == 1:
        #     self.life_sprites[2].opacity = 0
        #     self.life_sprites[1].opacity = 0
        # if self.ship.hp == 0:
        #     self.life_sprites[2].opacity = 0
        #     self.life_sprites[1].opacity = 0
        #     self.life_sprites[0].opacity = 0

        # Ici pour si on avait fait ça avec du texte:
        # if self.ship.hp != 3:
        #     self.life_text.text = f"Life: {self.ship.hp}"

        if self.ship.hp < 1:
            self.game_over_text.text = "GAME OVER"
        else:
            self.game_over_text.text = ""

            
class SpaceElement(Sprite):

    def __init__(self, image, position, image_anchor, initial_speed = [0, 0], collision_shape = "rectangle"):
        super().__init__(image, position, anchor = image_anchor, collision_shape = collision_shape)
        # ici on a mis anchor = anchor, parce que dans la classe Sprite, à cette place on a Scale,
        # donc on lui dit bien que anchor (de mon objet) se réfère à anchor (de la classe).
        self.speed = initial_speed


    def update(self, dt):
    # dt donne le temps qui s'est passé (en sec) entre un appel d'update (= un frame) et le suivant
        super().update(dt)

        x, y = self.position
        speed_x, speed_y = self.speed

        x += speed_x * dt
        y += speed_y * dt
        
        self.position = x, y

        if y > RESOLUTION[1] + 64:
            y = -64
        elif y < -64:
            y = RESOLUTION[1] + 64
        
        if x > RESOLUTION[0] + 64:
            x = -64
        elif x < -64:
            x = RESOLUTION[0] + 64
            
        self.position = x, y


class Asteroid(SpaceElement):

    def __init__(self, position, initial_speed, rotation_speed, level = 3):
        # Ici, observez la beauté de ces dictionnaires imbriqués:
        stats = {
            3: {
                "image": "sprites/asteroid128.png",
                "anchor": (64, 64)
                },
            2: {
                "image": "sprites/asteroid64.png",
                "anchor": (32, 32)
                },
            1: {
                "image": "sprites/asteroid32.png",
                "anchor": (16, 16)
                },
        }
        self.level = level
        image = stats[self.level]["image"]
        anchor = stats[self.level]["anchor"]                    
                                   
        super().__init__(image, position, anchor, initial_speed, "circle")
        self.rotation_speed = rotation_speed


    def update(self, dt):
        super().update(dt)
        self.rotation += self.rotation_speed * dt


    def pop_asteroid(self):
        level = self.level - 1
        if level <= 0: 
            return
        
        speed_x = randint(-20, 20)
        speed_y = randint(-20, 20)
        astero_speed = speed_x, speed_y
        astero_rotation_speed = randint(-20, 20)

        asteroid = Asteroid(self.position, astero_speed, astero_rotation_speed, level)
        self.layer.add(asteroid)


    def on_collision(self, other):
        super().on_collision(other)
        if isinstance(other, Ship):
            other.destroy()


    def destroy(self):
        super().destroy()
        for _ in range(3):
            self.pop_asteroid()
        

class Ship(SpaceElement):

    def __init__(self, position):
        super().__init__("sprites/ship.png", position, (32, 64), collision_shape = "circle")
        self.hp = 3
        self.rotation_speed = 0
        self.acceleration = 0
        self.shooting = False
        self.cooldown = 0.0
        self.invincible = 0.0


    def update(self, dt):
        speed_x, speed_y = self.speed
        angle = radians(-self.rotation + 90)
        acc_y = sin(angle) * self.acceleration
        acc_x = cos(angle) * self.acceleration

        speed_x += acc_x * dt
        speed_y += acc_y * dt

        self.speed = speed_x, speed_y
        super().update(dt)
        self.rotation += self.rotation_speed * dt

        if self.shooting:
            if self.cooldown <= 0:
                self.shoot()
                self.cooldown = 0.25
            else:
                self.cooldown -= dt

        if self.invincible > 0.0:
            self.invincible -= dt
            self.opacity = 125
        else:
            self.opacity = 255


    def shoot(self):
        bullet_speed = 300
        angle = radians(-self.rotation + 90)

        speed_x = cos(angle) * bullet_speed
        speed_y = sin(angle) * bullet_speed

        bullet = Bullet(self.position, [speed_x, speed_y], self.rotation)

        self.layer.add(bullet)


    def on_key_press(self, k, modifiers):
        if k == key.RIGHT:
            self.rotation_speed += 180
        if k == key.LEFT:
            self.rotation_speed -= 180
        if k == key.UP:
            self.acceleration = 100
        if k == key.RCTRL or k == key.LCTRL:
            self.shooting = True


    def on_key_release(self, k, modifiers):
        if k == key.RIGHT:
            self.rotation_speed -= 180
        if k == key.LEFT:
            self.rotation_speed += 180
        if k == key.UP:
            self.acceleration = 0
        if k == key.RCTRL or k == key.LCTRL:
            self.shooting = False


    def destroy(self):
        if self.invincible <= 0.0:
            self.hp -= 1
        
            if self.hp <= 0:
                super().destroy()
            else:
                self.invincible = 3.0


class Bullet(SpaceElement):

    def __init__(self, position, initial_speed, rotation):
        super().__init__("sprites/bullet.png", position, (8, 8), initial_speed)
        self.rotation = rotation
        self.life_time = 3.0 


    def on_collision(self, other):
        super().on_collision(other)
        if isinstance(other, Asteroid):
            other.destroy()
            self.destroy()


    def update(self, dt):
        super().update(dt)
        self.life_time -= dt
        if self.life_time <= 0: 
            # Ce serait très difficile de tomber exactement sur 0,
            # à cause des calculs du dt basés sur les frames.
            self.destroy()
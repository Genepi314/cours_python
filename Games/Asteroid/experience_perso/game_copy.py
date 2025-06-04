from if3_game.engine import Sprite
from pyglet.window import key
from math import radians, cos, sin
from random import randint


RESOLUTION = [800, 600]
CENTER = [RESOLUTION[0]/2, RESOLUTION[1]/2]


class SpaceElement(Sprite):

    def __init__(self, image, position, anchor, initial_speed = [0, 0], collision_shape = "rectangle"):
        super().__init__(image, position, anchor, collision_shape)
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

    def __init__(self, position, initial_speed, rotation_speed = 0):
        super().__init__("sprites/asteroid128.png", position, (64, 64), initial_speed, "circle")
        self.rotation_speed = rotation_speed

    def update(self, dt):
        super().update(dt)
        self.rotation += self.rotation_speed * dt

    def on_collision(self, other):
        super().on_collision(other)
        if isinstance(other, Ship):
            other.destroy()
            
    def destroy(self):

        super().destroy()

        a1 = SmallAsteroid(self.position, (randint(-200, 200), randint(-200,200)), 20)
        a2 = SmallAsteroid(self.position, (randint(-200, 200), randint(-200, 200)), 20)
        a3 = SmallAsteroid(self.position, (randint(-200, 200), randint(-200, 200)), 20)

        
        self.layer.add(a1)
        self.layer.add(a2)
        self.layer.add(a3)
    
        # dans on_collision, on a préalablement demandé en deuxième argument other
        

class SmallAsteroid(Asteroid):

    def __init__(self, position, initial_speed, rotation_speed):
        super().__init__("sprites/asteroid64.png", )
    
         

class Ship(SpaceElement):

    def __init__(self, position):
        super().__init__("sprites/ship.png", position, (32, 64), collision_shape = "circle")
        self.rotation_speed = 0
        self.acceleration = 0
        self.shooting = False
        self.cooldown = 0.0

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
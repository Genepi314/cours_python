from if3_game.engine import Sprite
from random import choice


RESOLUTION = [640, 480]

class PongSprite(Sprite):

    def __init__(self, image, position, anchor=(0,0), color=(255,255,255), collision_shape="rectangle"):
        
        image = f"sprites/{image}.png" 
        super().__init__(image, position, anchor=anchor, collision_shape=collision_shape)
        self.color = color


class PongPlayer(PongSprite):
    
    def __init__(self, position, color, speed, keys_move):

        super().__init__("player", position, anchor=(8,32), color=color)
        self.speed = speed
        self.key_up, self.key_down = keys_move 
        self.movement = 0

    def move(self, move_y):
        x, y = self.position
        y += move_y
        self.position = x, y

        rect = self.get_rect()
        if rect.top >= RESOLUTION[1]:
            y = RESOLUTION[1] - rect.height / 2
        elif rect.bottom <= 0: 
            y = rect.height / 2

        self.position = x, y

    def update(self, dt):
        super().update(dt)

        move_y = self.speed * self.movement * dt
        self.move(move_y)

    def on_key_press(self, key, modifiers):
        if key == self.key_down:
            self.movement = -1
        elif key == self.key_up:
            self.movement = 1

    def on_key_release(self, key, modifiers):
        if key == self.key_down and self.movement == -1:
            self.movement = 0
        elif key == self.key_up and self.movement == 1:
            self.movement = 0


class PongBall(PongSprite):

    def __init__(self, position, color, speed, cooldown=3.0):

        super().__init__("ball", position, anchor=(8,8), color=color)
        self.speed = list(speed) # si speed était un tuple, il devient une list
        self.start_position = position
        self.start_color = color
        self.cooldown = cooldown
        self.reset()

    def reset(self):
        self.position = self.start_position
        self.speed = [choice([-1 , 1]) * self.speed[0], choice([-1 , 1]) * self.speed[0]]
        self.color = self.start_color
        self.__time = self.cooldown

    def on_collision(self, other):
        super().on_collision(other)
        if isinstance(other, PongPlayer):
            self.speed[0] *= -1
            self.speed[1] += other.movement * other.speed / 5
            self.color = other.color

    def update(self, dt):
        super().update(dt)

        if self.__time > 0.0:
            self.__time -= dt
            return 
        
        x, y = self.position
        sx, sy = self.speed

        x += sx * dt
        y += sy * dt

        self.position = x, y

        rect = self.get_rect()

        if rect.right >= RESOLUTION[0] or rect.left <= 0:
            self.reset()
            return

        rect = self.get_rect()
        if rect.top >= RESOLUTION[1]:
            y = RESOLUTION[1] - rect.height / 2
            self.speed[1] *= -1
        elif rect.bottom <= 0: 
            y = rect.height / 2
            self.speed[1] *= -1

        self.position = x, y

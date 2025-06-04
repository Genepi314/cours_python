from if3_game.engine import Sprite, Layer, Text
from random import choice, randint
from math import cos, sin, radians


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
        self.new_speed = 100   
        self.reset()
        self.score1 = 0
        self.score2 = 0

    def reset(self):
        self.position = self.start_position
        
        self.angle = randint(0,360)

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
        self.speed = list(self.speed)

        if self.__time > 0.0:
            self.__time -= dt
            return 
        
        speed_x, speed_y = self.speed
        pos_x, pos_y = self.position

        dir_x = cos(self.angle)* speed_x * dt
        dir_y = sin(self.angle) * speed_y * dt

        self.speed = [speed_x, speed_y]

        pos_x += dir_x 
        pos_y += dir_y

        self.position = pos_x, pos_y

        rect = self.get_rect()

        if rect.right >= RESOLUTION[0]:
            self.reset()
            self.score1 += 1
            return

        elif rect.left <= 0:
            self.reset()
            self.score2 += 1

            return

        rect = self.get_rect()
        if rect.top >= RESOLUTION[1]:
            pos_y = RESOLUTION[1] - rect.height / 2
            self.speed[1] *= -1
        elif rect.bottom <= 0: 
            pos_y = rect.height / 2
            self.speed[1] *= -1

        self.position = pos_x, pos_y


class UILayer(Layer):
    def __init__(self, ball ,p1, P1_COLOR, p2, P2_COLOR):
        super().__init__()
        self.ball = ball

        self.score_p1 = Text("Player 1 : ",(20, 430),color=P1_COLOR,anchor="top, left")
        self.add(self.score_p1)
        self.score_p2 = Text("Player 2 : ",(520, 430),color=P2_COLOR,anchor="top, right")
        self.add(self.score_p2)

    def update(self, dt):
        super().update(dt)
        
        self.score_p1.text = f"Player 1 : {self.ball.score1}"
        self.score_p2.text = f"Player 2 : {self.ball.score2}"

from if3_game.engine import Sprite, Layer, Text
from random import choice, randint
from math import radians, cos, sin


RESOLUTION = [640, 480]


class UILayer(Layer):

    def __init__(self, ball):
        super().__init__()
        self.ball = ball
        
        self.score_text1 = Text(f"Player 1: {self.ball.p1_score}", (10, 450), 20)
        self.score_text2 = Text(f"Player 2: {self.ball.p2_score}", (500, 450), 20)
        self.add(self.score_text1, self.score_text2)


    def update(self, dt):
        super().update(dt)
        self.score_text1.text = f"Player 1: {self.ball.p1_score}"
        self.score_text2.text = f"Player 2: {self.ball.p2_score}"


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
        self.score = 0

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
        self.p1_score = 0
        self.p2_score = 0
        self.reset()

    def reset(self):

        self.rotation = randint(0, 360)

        self.position = self.start_position
        self.speed = 100, 100
        speed_x, speed_y = self.speed

        angle = radians(-self.rotation + 90)

        speed_x = cos(angle) * speed_x
        speed_y = sin(angle) * speed_y

        self.speed = [speed_x, speed_y]

        #self.speed = [choice([-1 , 1]) * self.speed[0], choice([-1, 1]) * self.speed[0]]
        self.color = self.start_color
        self.__time = self.cooldown

    def on_collision(self, other):
        super().on_collision(other)
        acceleration = 1.3
        if isinstance(other, PongPlayer):
            self.speed[0] *= -1 * acceleration
            self.speed[1] += other.movement * other.speed / 5 * acceleration
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

        if rect.right >= RESOLUTION[0]:
            self.p1_score += 1
            self.reset()
            return
        
        if rect.left <= 0:
            self.p2_score += 1
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

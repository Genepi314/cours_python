from if3_game.engine import Game, Layer, init
from pyglet.window import key
from pong_copy import RESOLUTION, PongPlayer, PongSprite, PongBall, UILayer

# --- constants ---

PLAYER_SPEED_y = 300

P1_POS = 30, RESOLUTION[1] / 2
P1_COLOR = 0, 200, 200 # cyan
P1_KEYS = key.Z, key.S

P2_POS = RESOLUTION[0] - 30, RESOLUTION[1] / 2
P2_COLOR = 200, 0, 200 # magenta
P2_KEYS = key.UP, key.DOWN

PLAYGROUND_COLOR = 200, 200, 0 # yellow

BALL_POSITION = RESOLUTION[0] / 2, RESOLUTION[1] / 2
BALL_COLOR = 200, 200, 200
BALL_SPEED = 100, 100

# --- game ---

init(RESOLUTION, "Pong")

playground = Layer()
playground.add(PongSprite("playground", (0, 0), color=PLAYGROUND_COLOR))

game_layer = Layer()
p1 = PongPlayer(P1_POS, P1_COLOR, PLAYER_SPEED_y, P1_KEYS)
p2 = PongPlayer(P2_POS, P2_COLOR, PLAYER_SPEED_y, P2_KEYS)

ball = PongBall(BALL_POSITION, BALL_COLOR, BALL_SPEED)

uilayer = UILayer(ball)

game_layer.add(p1, p2, ball)

game = Game()
game.add(playground, uilayer, game_layer)

game.run()
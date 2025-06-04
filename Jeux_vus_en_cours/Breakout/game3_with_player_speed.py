import pgzrun

WIDTH = 800
HEIGHT = 600
TITLE = "Bizou"


all_blue_bricks = []

for x in range(150, 750, 100):
    blue_brick = Actor("blue_brick")
    blue_brick.pos = [x, 250]
    blue_brick.hp = 3
    all_blue_bricks.append(blue_brick)


ball = Actor("ball")
ball.pos = [400, 300] 
# On pourrait aussi écrire:
# ball.x = 400
# ball.py = 300
ball_speed = [3, -3]


player = Actor("player")
player.pos = [400, 550]

all_bricks = []

lines = 7
for  y in range(0, 30 * lines, 30):
    for x in range(0, 800, 100):
        brick = Actor("brick", anchor = ["left", "top"])
        brick.pos = [x, y]
        all_bricks.append(brick)

# On peut aussi dessiner un cercle.
# circle_position = [400, 300]

def invert_horizontal_speed():
    ball_speed[0] *= -1


def invert_vertical_speed():
    ball_speed[1] *= -1


def update():
    
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]
    

    # print(ball.x)
    # Cette ligne ci-dessus montre que l'ordinateur continue de calculer la position de la balle bieeen au-delà de la taille de l'écran !!

    if ball.y < 0 or ball.y > HEIGHT:
        invert_vertical_speed()

    if ball.x > WIDTH or ball.x < 0:
        invert_horizontal_speed()

    if ball.colliderect(player):
        invert_vertical_speed()

    for brick in all_bricks:
        if ball.colliderect(brick):
            invert_vertical_speed()
            all_bricks.remove(brick)

    for blue_brick in all_blue_bricks:
        if blue_brick.hp > 0:
            if ball.colliderect(blue_brick):
                invert_vertical_speed()
                blue_brick.hp -= 1
           
            
            
# draw DOIT être là, et la fonction est appelée automatiquement une fois définie.
def draw():
    screen.clear()
    for brick in all_bricks:
        brick.draw()
    ball.draw()
    player.draw()
    for blue_brick in all_blue_bricks:
        if blue_brick.hp > 0:
            blue_brick.draw()


def on_mouse_move(pos):
    # print(pos)
    # print(pos[0])
    # On prend avec pos[0] l'index "0" de la "liste" qui reprend les coordonnées [x, y] de la souris! 
    # player.pos = [pos[0], 550]
    # Et ici, on réassigne la valeur 550 à l'index "1" (y) à la liste des coordonnées de la souris.
    player.x = pos[0]




pgzrun.go()

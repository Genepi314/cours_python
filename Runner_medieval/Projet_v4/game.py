# game data

from random import randint
import pgzero.keyboard
import pgzero.music
import pgzrun, pgzero
import pgzhelper
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'


screen: pgzero.screen.Screen
Actor: pgzero.actor.Actor
keys: pgzero.keyboard.keys
music: pgzero.music._music


WIDTH = 800
HEIGHT = 600

GROUND = 458
gravity = 250
downward_gravity = 500

NUMBER_OF_BACKGROUND = 2

######## Gene : Tweaks pour la jouabilité (GAMESPEED) et ajouts ########
GAME_SPEED = 240
INVINCIBILITY = 2
CHALLENGER_JUMP = 175
########################################################################

JUMP_SPEED = 250

######## Gene : Un game_state ########

music.play("lully")
game_state = "startscreen"

# écran start

startscreen = Actor("startscreen", anchor=('middle', 'center'))
startscreen.pos = WIDTH/2, HEIGHT/2

calque = Actor("calquee", anchor=('middle', 'center'))
calque.pos = WIDTH/2, HEIGHT/2

calque_sombre = Actor("calquee2", anchor=('middle', 'center'))
calque_sombre.pos = WIDTH/2, HEIGHT/2

# hero initialisation

hero = Actor("chevalier", anchor=('middle', 'bottom'))
hero.pos = (32, GROUND)
hero_speed = 0

######## Gene : Les pv du héros ########
hero.pv = 3
hero.invincibility = 0
########################################

######## Gene : AFFICHAGE pv ########
pv_sprites = []
####################################################

# enemies initialisations

# BOX_APPARTION = (2, 5)
# next_box_time = randint(BOX_APPARTION[0], BOX_APPARTION[1])
boxes = []

#------------------#
# Objet défilement #
#------------------#

ovni = Actor("mouette-gauche.png", anchor=('left', 'top'))
ovni.pos =(HEIGHT, 100)
ovni_reapparition_time = 5
ovni_timer = 0
ovni_visible = True 

######## Gene : Init challenger ########
CHALLENGER_APPARITION = (3, 7)
next_challenger_time = randint(CHALLENGER_APPARITION[0], CHALLENGER_APPARITION[1])
challengers = []
challenger_speed = 0 
########################################

# background inititalisation

backgrounds_bottom = []
backgrounds_top = []

# barbaric lower background connect fix

barbaric_background_fix = 0     #AJOUT

def draw():
    screen.clear()

    ######## Estelle : écran start ########
    if game_state == "startscreen":
        startscreen.draw()
        return
    
    for bg in backgrounds_bottom:
        bg.draw()

    for bg in backgrounds_top:
        bg.draw()

    for box in boxes:
        box.draw()

    #------------------#
    # Objet défilement #
    #------------------#
    ovni.draw()

    ######## Gene : draw challengers ########
    for challenger in challengers:
        challenger.draw()

    ######## Gene : AFFICHAGE pv ########
    for pv_sprite in pv_sprites:
        pv_sprite.draw()
    #####################################

    ######## Gene : écran du game over ########
    if game_state == "game over":
        # insert sprite heros mort et background
        calque_sombre.draw()
        screen.draw.text("GAME\nOVER", 
            center=(WIDTH/2, HEIGHT/2 -70),
            fontsize = 80,
            fontname = "goudysto",
            color='red'
        )
        screen.draw.text("PRESS SPACE TO TRY AGAIN", 
            center=(WIDTH/2, HEIGHT/2 + 145),
            fontsize =20,
            fontname = "goudysto",
            color=(248,248,215)
        )
        hero.draw() 
    elif game_state == "pause":
        hero.draw() 
        calque.draw()
        screen.draw.text(
            "PAUSE",
            center=(WIDTH/2, HEIGHT/2),
            fontsize = 60,
            fontname = "goudysto",
            color=(238,238,205)
        )
    elif game_state == "play":
        hero.draw() 


def update(dt):
    ######## Gene : freeze pour game over ########
    global game_state
    global hero 

    if game_state == "game over": 
        hero = Actor("dead_hero", anchor=('middle', 'bottom'))
        hero.pos = (64, GROUND)
        return
    elif game_state == "pause":
        return
    elif game_state == "startscreen":
        return
    
    if game_state == "start":
        start()
        game_state = "play"
        return

    ######## Gene : cooldown pour pv ########
    if hero.invincibility > 0:
        hero.invincibility -= dt
    else:
        hero.invincibility = 0

    if hero.invincibility <= 0:
        hero.image = "chevalier"
    else:
        hero.image = "chevalier-blesse"    

    global next_challenger_time
    global challenger
    global challenger_speed

    ######## Gene : challenger: comportement bah ouais ########
    next_challenger_time -= dt
    if next_challenger_time <= 0:
        challenger = Actor("poule", anchor=('left', 'bottom'))
        challenger.pos = WIDTH, GROUND
        challenger.speed = 0
        challengers.append(challenger)
        next_challenger_time = randint(CHALLENGER_APPARITION[0], CHALLENGER_APPARITION[1])

    for challenger in challengers:
        challenger_gravity = 200

        x, y = challenger.pos
        x -= GAME_SPEED * dt
        
        if y > GROUND:
            y = GROUND
            challenger.speed = 0

        if y == GROUND:
            # challenger_speed = CHALLENGER_JUMP
            challenger.speed = CHALLENGER_JUMP
            
        challenger.speed -= challenger_gravity * dt 
        y -= challenger.speed * dt

        challenger.pos = x, y

    ######## Gene : petite mise à jour ici vu qu'on a un système de pv ########
        if challenger.colliderect(hero) and hero.invincibility == 0:
            hero.invincibility = INVINCIBILITY
            hero.pv -= 1
            ######## Gene : AFFICHAGE pv ########
            pv_sprites.pop()

    if challengers:
        if challengers[0].pos[0] <= - 32:
            challengers.pop(0)
    ############################################################################

    # enemies update
    # box
    global next_box_time

    next_box_time -= dt
    if next_box_time <= 0:
        box = Actor("bottedefoin", anchor=('left', 'bottom'))
        box.pos = WIDTH, GROUND
        boxes.append(box)
        next_box_time = randint(BOX_APPARTION[0], BOX_APPARTION[1])

    for box in boxes:
        x, y = box.pos
        x -= GAME_SPEED * dt
        box.pos = x, y
        ######## Gene : petite mise à jour ici vu qu'on a un système de pv ########
        if box.colliderect(hero) and hero.invincibility == 0:
            hero.invincibility = INVINCIBILITY
            hero.pv -= 1
            ######## Gene : AFFICHAGE pv ########           
            pv_sprites.pop()
        ###########################################################################

    if boxes:
        if boxes[0].pos[0] <= - 32:
            boxes.pop(0)

    #------------------#
    # Objet défilement #
    #------------------#
    global ovni_timer, ovni_visible
    if ovni_visible:
        x, y = ovni.pos
        x -= (GAME_SPEED*2) *dt
        ovni.pos = x, y

        if ovni.pos[0] <= -ovni.width:
            ovni_visible = False
            ovni_timer = ovni_reapparition_time
    else:
        ovni_timer -= dt
        if ovni_timer <= 0:
            ovni_visible = True
            ovni.pos = (WIDTH, 100)

    # hero update

    global hero_speed, downward_gravity, gravity

    hero_speed -= gravity * dt
    x, y = hero.pos
    y -= hero_speed * dt

    if y < 350:
        hero_speed = -10 

    if hero_speed < 0 and y < GROUND:
        gravity = downward_gravity

    if y > GROUND:
        y = GROUND
        hero_speed = 0
        gravity = 200

    hero.pos = x, y

    # bg update

    global barbaric_background_fix      #AJOUT

    for bg in backgrounds_bottom:
        x, y = bg.pos
        x -= GAME_SPEED * dt
        bg.pos = x, y

    if backgrounds_bottom[0].pos[0] <= - WIDTH:
        barbaric_background_fix += 1.5
        bg = backgrounds_bottom.pop(0)
        bg.pos = backgrounds_bottom[0].pos[0] + WIDTH, HEIGHT
        backgrounds_bottom.append(bg)

    for bg in backgrounds_top:
        x, y = bg.pos
        x -= GAME_SPEED/3 * dt
        bg.pos = x, y

    if backgrounds_top[0].pos[0] <= - WIDTH:
        bg = backgrounds_top.pop(0)
        bg.pos = (NUMBER_OF_BACKGROUND - 1) * WIDTH, 0
        backgrounds_top.append(bg)
    
    if hero.pv == 0:
        music.play("death_hit")
        music.fadeout(1.5)
        music.play("barricades")
        game_state = "game over"
    
    if next_challenger_time < 1 and next_box_time < 1:       
        next_challenger_time += 1


def on_key_down(key):
    global hero_speed, game_state

    # jump
    if game_state == "play":
        if key == keys.SPACE:

    ######## Gene : bug double saut corrigé ########
            if hero.pos[1] == GROUND:
                hero_speed = JUMP_SPEED
    ################################################

    #space to start
    if game_state == "startscreen":
        if key == keys.SPACE:
            game_state = "start"
    
    if game_state == "game over":
        #le chevalier prend un coup fatal

        if key == keys.SPACE:
            game_over()
            game_state = "start"
            reset()

    #-------#
    # PAUSE #
    #-------#

    if key == pgzero.keyboard.keys.ESCAPE:
        if game_state != "pause":
            game_state = "pause"
        else:
            game_state = "play"

        # Juste pour tester le game over
    # if key == key.RETURN:
    #     game_state = "game over"

######## Gene : fonction game_over() et dépendances ########
def game_over():
    global hero
    global boxes
    global challengers
    global backgrounds_bottom
    global backgrounds_top
    global game_state

    #retour à l'écran titre dans on_key_down

    boxes = []
    challengers = []
    backgrounds_bottom = []
    backgrounds_top = []

############################################################

######################################
##### Estelle : fonction start() #####
######################################
def start():
    global pv_sprites
    pv_sprites = []

    # Le chevalier part en mission
    if music:
        music.fadeout(0.5)
    music.play("francoeur_violon_clav")

    # # global NUMBER_OF_BACKGROUND         #SUPPRIMÉ
    # for n in range(NUMBER_OF_BACKGROUND):     #SUPPRIMÉ
    bg_b1 = Actor("sol1", anchor=('left', 'bottom'))
    bg_b1.pos = 0, HEIGHT
    backgrounds_bottom.append(bg_b1)

    bg_b2 = Actor("sol2", anchor=('left', 'bottom'))
    bg_b2.pos = WIDTH, HEIGHT
    backgrounds_bottom.append(bg_b2)

    bg_t1 = Actor("arriereplan1", anchor=('left', 'top'))
    bg_t1.pos = 0, 0
    backgrounds_top.append(bg_t1)

    bg_t2 = Actor("arriereplan2", anchor=('left', 'top'))
    bg_t2.pos = WIDTH, 0
    backgrounds_top.append(bg_t2)

    ######## Gene : AFFICHAGE pv ########

    for n in range(hero.pv):
        pv_sprite = Actor("potion30px", anchor=('left', 'bottom'))
        pv_sprite.pos = 30, 30
        x, y = pv_sprite.pos
        x += 30 * n
        pv_sprite.pos = x, y
        pv_sprites.append(pv_sprite)
    #####################################

    global BOX_APPARTION
    BOX_APPARTION = (2, 5)
    
    global next_box_time

    startbox1= Actor("bottedefoinaveccible", anchor=('left', 'bottom'))          #AJOUT
    startbox1.pos = 3 * WIDTH / 4, GROUND                               #AJOUT
    boxes.append(startbox1)                                             #AJOUT
    
    next_box_time = randint(BOX_APPARTION[0], BOX_APPARTION[1])

def reset():
    hero.pv = 3
    hero.invincibility = 0
    hero.image = "chevalier"
    start()

pgzrun.go()
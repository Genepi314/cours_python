from if3_game.engine import Game, Layer, init, Sprite
from game import Asteroid, RESOLUTION, CENTER, Ship, UILayer, AsteroidGame

init(RESOLUTION, "Asteroid")

# s1 = Asteroid((100, 200), (-50, -200), 20)
# s2 = Asteroid((750, 500), (50, 200), 20)
# ship = Ship(CENTER)


# background_layer = Layer()
# background_layer.add(Sprite("sprites/background.jpg"))

# game_layer = Layer()
# game_layer.add(s1, s2, ship)

# ui_layer = UILayer(ship)

# game = Game()
# Attention, l'ordre a de l'importance, il les charge dans l'ordre et les superpose:
# game.add(background_layer, game_layer, ui_layer)
# game.debug = True
game = AsteroidGame()
game.run()
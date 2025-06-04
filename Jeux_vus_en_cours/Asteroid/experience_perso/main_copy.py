from if3_game.engine import Game, Layer, init
from game_copy import Asteroid, RESOLUTION, CENTER, Ship

init(RESOLUTION, "Asteroid")

s1 = Asteroid("sprites/asteroid128.png", (100, 200), (-50, -200), 20)
s2 = Asteroid("sprites/asteroid128.png", (750, 500), (50, 200), 20)
ship = Ship(CENTER)

game_layer = Layer()
game_layer.add(s1, s2, ship)

game = Game()
game.add(game_layer)
game.debug = True

game.run()
# Ou comment fonctionne un moteur de jeu en background sur les fonctions Update() et Draw() etc

class GameObject:
    def __init__(self, name):
        self.name = name
        self.counter = 0

    def update(self):
        self.counter += 1

    def draw(self):
        print(f"{self.name} = {self.counter}") 

objects = []

objects.append(GameObject("First"))
objects.append(GameObject("Second"))
objects.append(GameObject("Third"))

while True:
    # Read input, truc géré par le moteur de jeu pour lire le clavier etc
    # Update
    for obj in objects:
        # Idéalement on devrait mettre une condition pour vérifier que les objets ont bien une fonction Update()
        obj.update() 
    # Draw
    for obj in objects:
        obj.draw()
class Flower:
    
    def __init__(self):
        self.growth = 0
        self.max_growth = 3
        self.times = 0
        self.total_times = 0
        self.initial_price = 5
        self.sell_price = 5

    def water(self):
        self.times += 1
        self.total_times += 1
        if self.times == 3:
            self.growth += 1
            self.times = 0
        self.growth = min(self.growth, self.max_growth)

    def sell(self):
        self.sell_price = self.initial_price * self.growth
       

# -- main part --


f = Flower()

while f.growth != f.max_growth:
    f.water()
f.sell()
print(f"Vous avez arrosé votre géranium {f.total_times} fois.\nIl vaut maintenant {f.sell_price} euros.")




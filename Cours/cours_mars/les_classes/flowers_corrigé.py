class Flower:
    
    def __init__(self):
        self.growth = 0
        self.max_growth = 3
        self.times = 0
        self.initial_price = 5
        self.sell_price = 5

    def water(self):
        self.times += 1
        if self.times % 3 == 0 :
            self.growth += 1
        self.growth = min(self.growth, self.max_growth)

    def sell(self):
        self.sell_price = self.initial_price * self.growth

f = Flower()
while f.growth < f.max_growth:
    f.water()


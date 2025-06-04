from vehicles3 import Vehicle
# class Vehicle:

#     def __init__(self, speed):
#        self.speed = speed
#        self.distance = 0

#    def ride(self, duration):
#        self.distance += duration * self.speed


class Train(Vehicle):

    def __init__(self, max_capacity):
        super().__init__(150)
        self.passengers = 0
        self.max_capacity = max_capacity
        
    def take_on_board(self, passengers):
        self.passengers += passengers
        # Ci-dessous, on choisit la plus petite valeur entre les deux variables, puisqu'on ne veut pas excéder la max_capacity
        self.passengers = min(self.passengers, self.max_capacity)
        # On pourrait aussi écrire 
        # if self.passengers > self.max_capacity:
            # self.passengers = self.max_capacity


class Intercity(Train):

    def __init__(self):
        super().__init__(100)
        self.profit_by_kilometer = 2.5
        self.profit = 0

    def ride(self, duration):
        super().ride(duration)
        self.profit = self.profit_by_kilometer * self.distance


class FreightTrain(Train):

    def __init__(self):
        super().__init__(4)
        self.cargo = 0

    def load_cargo(self, cargo):
        self.cargo += cargo
        




# freight1 = FreightTrain()
# freight1.load_cargo(5)
# print(freight1.cargo)


t = Train(10)
t.ride(5)

print(t.distance)
print(t.max_capacity)

t.take_on_board(5)
t.take_on_board(3)

print(t.passengers)

ic3232 = Intercity()




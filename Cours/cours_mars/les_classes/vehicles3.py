class Vehicle:

    def __init__(self, speed):
        self.speed = speed
        self.distance = 0

    def ride(self, duration):
        self.distance += duration * self.speed


class Car(Vehicle):

    def __init__(self):
        super().__init__(100)
        self.fuel = 100
        self.consumption = 0.05

    def ride(self, duration):
        ideal_distance = duration * self.speed
        maximum_distance = self.fuel / self.consumption
        real_distance = min(ideal_distance, maximum_distance)
        self.distance += real_distance
        self.fuel -= self.consumption * real_distance

c = Car()
c.ride(5)
print(c.distance, c.fuel)
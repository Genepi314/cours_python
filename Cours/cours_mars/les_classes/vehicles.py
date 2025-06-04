class Bike:
    def __init__(self):
        self.speed = 15
        self.distance = 0

    def ride(self, duration):
        self.distance += duration * self.speed
# ou le code écrit dans les slides

b = Bike()
b.ride(2)
print(b.distance)

class Car:
    def __init__(self):
        self.speed = 100
        self.distance = 0

    def ride(self, duration):
        self.distance += duration * self.speed

c = Car()
c.ride(3)
print(c.distance)
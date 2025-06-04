class Vehicle:

    def __init__(self, speed):
        self.speed = speed
        self.distance = 0

    def ride(self, duration):
        self.distance += duration * self.speed
    

# b pour bike, voir vehicles.py
b2 = Vehicle(15)
b2.ride(2)
print(b2.distance)

class Bike(Vehicle):

    def __init__(self):
        super().__init__(15)


b2 = Bike()
b2.ride(2)
print(b2.distance)


class Car(Vehicle):

    def __init__(self):
        super().__init__(100)


honda = Car()
honda.ride(5)
print(honda.distance)
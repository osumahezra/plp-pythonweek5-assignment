class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Car(Vehicle):
    def move(self):
        print("Driving on the road")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky")

class Boat(Vehicle):
    def move(self):
        print("Sailing on the water")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling on the path")


# Polymorphic behavior
vehicles = [Car(), Plane(), Boat(), Bicycle()]

for vehicle in vehicles:
    vehicle.move()
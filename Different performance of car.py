class car:
    def __init__(self,name):
        self.name = name
        
    def drive(self):
        raise NotImplementedError ("Sub Class Must Implement abstract method")
    def stop(self):
        raise NotImplementedError ("Sub Class Must Implement abstract method")
    
class Truck(car):
    def drive(self):
        return "Drive Slowly"
    def stop(self):
        return "Truck Breaking"
    
class sportcar(car):
    def drive(self):
        return "Drive Fast"
    def stop(self):
        return "sportcar breaking"
    
obj_truck = Truck("Truck Car")
print(obj_truck.drive())
print(obj_truck.stop())
obj_spot = sportcar("Spot Car")
print(obj_spot.drive())
print(obj_spot.stop())

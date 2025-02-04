class MotorCycle: 
  
    """Class for MotorCycle"""
  
    def __init__(self): 
        self.name = "MotorCycle"
  
    def TwoWheeler(self): 
        return "TwoWheeler"
  
  
class Truck: 
    def __init__(self):
        self.name = 'Truck'

    def EightWheeler(self):
        return 'EightWheeler'


class Car:
    def __init__(self):
        self.name = 'Car'

    def FourWheeler(self):
        return 'FourWheeler'
  
class Adapter: 

    def __init__(self, obj, **adapted_methods):
        self.name = obj.name
        self.adapter = adapted_methods
  
    def __getattr__(self, attr): 
        return self.adapter[attr]
  
    
objects = []
motorCycle = MotorCycle()
objects.append(Adapter(motorCycle, wheels = motorCycle.TwoWheeler))
truck = Truck()
objects.append(Adapter(truck, wheels = truck.EightWheeler))
car = Car()
objects.append(Adapter(car, wheels = car.FourWheeler))
for obj in objects:
    print("A {0} is a {1} vehicle".format(obj.name, obj.wheels()))
from abc import ABC, abstractmethod

class Product(ABC):
    
    @abstractmethod
    def cook(self):
        pass

class FettuccineAlfredo(Product):

    @classmethod
    def cook(cls,name = 'Fettuccine Alfredo'):
        print(f'Italian main course prepared: {name}')
        
class Tiramisu(Product):
        
    @classmethod
    def cook(cls, name='Tiramisu'):
        print(f"Italian dessert prepared: {name}")
    
class DuckALOrange(Product):
    
    @classmethod    
    def cook(cls, name= "Duck À L'Orange"):
        print(f"French main course prepared: {name}")
        
class CremeBrulee(Product):
    @classmethod
    def cook(cls, name= "Crème brûlée"):
        print(f"French dessert prepared: {name}")
        
class Factory(ABC):
    
    @abstractmethod
    def get_dish(self, type_of_meal):
        return type_of_meal

class ItalianDishesFactory(Factory):
    
    @classmethod
    def get_dish(cls, type_of_meal):
        if type_of_meal == "main":
            return FettuccineAlfredo
        else:
            return Tiramisu

class FrenchDishesFactory(Factory):
    
    @classmethod
    def get_dish(cls, type_of_meal):
        if type_of_meal == "main":
            return DuckALOrange
        else:
            return CremeBrulee
    
    
class FactoryProducer:

    def get_factory(self, type_of_factory):
        if type_of_factory == 'italian':
            return ItalianDishesFactory
        else:
            return FrenchDishesFactory


    
fp = FactoryProducer()
fac = fp.get_factory("italian")
main_dish = fac.get_dish("main")
main_dish.cook()

fac1 = fp.get_factory("french")
main_dish = fac1.get_dish("main")
main_dish.cook()
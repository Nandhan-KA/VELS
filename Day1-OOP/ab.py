from abc import ABC, abstractmethod # ABC -  Abstract Base Class

class Vehicle(ABC):
    
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):  
        pass
    
    
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")
        
    def stop_engine(self):
        print("Car engine stopped")
        
        
car1=Car()
car1.start_engine() 
car1.stop_engine()
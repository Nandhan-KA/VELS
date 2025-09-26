# #single inheritance
# class Vehicle:
#     no_of_wheels=4
    
#     def start(self):
#         print("Vehicle started")
        
# class Car(Vehicle):
#     mileage = 24.5
    
# car1=Car()
# print(car1.mileage)
# print(car1.no_of_wheels)
# car1.start()


#hierarchical inheritance
class grandparent:
    def gp(self):
        print("Grandparent class")

class parent(grandparent):
    def p(self):
        print("Parent class")
    
class Child(parent):
    def c(self):
        print("Child class")
        
c1=Child()
c1.gp()
c1.p()
c1.c()  
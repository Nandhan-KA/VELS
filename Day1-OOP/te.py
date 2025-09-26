# class Vehicle:
    
#     no_of_wheels=4
#     mileage=25.0
#     cc=225
#     fuel_type="Petrol"
    
# car1=Vehicle()
# car1.no_of_wheels=6
# print(car1.no_of_wheels)
# car1.mileage=30.5
# print(car1.mileage)
# car1.cc=1500
# print(car1.cc)
# car1.fuel_type="Diesel" 
# print(car1.fuel_type)
# print(id(car1))

class Vehicle:
    def __init__(vels,no_of_wheels, mileage, cc, fuel_type):
        vels.no_of_wheels = no_of_wheels
        vels.mileage = mileage
        vels.cc = cc
        vels.fuel_type = fuel_type
        
    def display(vels):
        print("No of wheels:", vels.no_of_wheels)
        print("Mileage:", vels.mileage)
        print("CC:", vels.cc)
        print("Fuel type:", vels.fuel_type)

car1 = Vehicle(4, 30.5, 1500, "Diesel")
car1.display()


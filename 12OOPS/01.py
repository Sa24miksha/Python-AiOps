# BASIC CLASS AND OBJECT 
# create a car class with attribute brand and model . Then craete an instance of class 

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car_obj = Car("Toyota","Corolla")
print(car_obj.brand)
print(car_obj.model)

car_obj2 = Car("Tata", "Safari")
print(car_obj2.model)
print(car_obj2.brand)
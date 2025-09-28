# Create a class Car and add a class varible to track the numbers of Car created 

class Car:

    Total_Car = 0   # Class Varible 

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.Total_Car += 1

Car_obj1 = Car("Toyota", "Cornel")
Car_obj2 = Car("Hyundai", "Exter")
Car_obj3 = Car("Tata", "Nano")


print(Car.Total_Car)
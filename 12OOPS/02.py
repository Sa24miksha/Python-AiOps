# Geberate a method in the Car class that display the full name of the Car class (brand and model)

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"


car_obj1 = Car("Toyota", "Corolla")
print(car_obj1.full_name())
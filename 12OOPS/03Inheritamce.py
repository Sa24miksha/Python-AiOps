# Create an electricCar class that inherit from the Car Class and had an additional attribute 
# battery_size

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def full_name(self):
        return f"{self.brand} {self.model}"
    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size


my_Tesela = ElectricCar("Tesela", "Model S", "85kwh")
print(my_Tesela.model)
print(my_Tesela.full_name())
print(my_Tesela.battery_size)

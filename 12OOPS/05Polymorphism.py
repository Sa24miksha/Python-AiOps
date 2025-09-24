# Generate a method fuel type in both Car and Electric_Car classes but with differenet behaviour 

# Create an electricCar class that inherit from the Car Class and had an additional attribute 
# battery_size

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or diesel"
    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge!"
    

ElectricCar_obj = ElectricCar("Tesela", "Model S", "85kwh")
Car_obj = Car("Tata", "Safari")

print(ElectricCar_obj.fuel_type())
print(Car_obj.fuel_type())

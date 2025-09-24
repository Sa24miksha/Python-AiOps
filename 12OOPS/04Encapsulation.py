#  Modify the car, encapsulate the brand attribute and make it private and provide a getter 
# method of it 

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    # getter
    def get_brand(self):
        return self.__brand + "!"

    def full_name(self):
        return f"{self.__brand} {self.model}"
    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size


my_Tesela = ElectricCar("Tesela", "Model S", "85kwh")
# print(my_Tesela.__brand) --> not accessible now !
print(my_Tesela.get_brand())

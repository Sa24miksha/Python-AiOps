# PROPERTY DECORATOR 
# Use a property decorator in the car class to make the model attribute read-only

class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

Car_obj1 = Car("Toyota", "Cornel")

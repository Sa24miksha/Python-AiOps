# STATIC METHOD - belongs to class rather than the instance of the class !

# Add a static method to a Car class that return a general description of a car 

class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @staticmethod
    def general_description():
        return "The car is a vehicle with 4 wheel and is a means of transport!"

Car_obj1 = Car("Toyota", "Cornel")
print(Car.general_description())


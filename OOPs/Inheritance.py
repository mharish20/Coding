class Vehicle:
    def __init__(self,brand):
        self.brand = brand
    def drive(self):
        print(f"{self.brand} is driving.")
class Car(Vehicle):
    def __init__(self, brand,color):
        super().__init__(brand)
        self.color = color

car = Car("Suzuki","Black")
car.drive()
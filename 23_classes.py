class Vehicle:
    def __init__(self, brand: str, year: int):
        self.brand = brand
        self.year = year
        # self.wheels = wheels
    def print_my_info(self):
        print(f"This is a general print my info method")


class Car(Vehicle):
    def __init__(self, brand: str, year: int, wheels=4):
        super().__init__(brand, year)
        self.wheels = wheels

    # def print_my_info(self):
    #     print(f"This is a {self.brand} car with {self.wheels} wheels created on date {self.year}. ")


class Truck(Vehicle):
    def __init__(self, brand: str, year: int, wheels=8, hp=500):
        super().__init__(brand, year)
        self.wheels = wheels
        self.hp = hp

    def print_my_info(self):
        print(
            f"This is a {self.brand} truck with {self.wheels} wheels and created on year {self.year} with Horse powers equal {self.hp}. ")


bmw_car = Car("BMW", 2022, wheels=5)
# print(bmw_car.wheels)
# print(bmw_car.brand)
bmw_car.print_my_info()

vm_car = Car("volvo", 2013)
# print(vm_car.brand)
# print(vm_car.wheels)
vm_car.print_my_info()

vm_truck = Truck("Tatra", 2017)
vm_truck.print_my_info()


class Car:

    def __init__(self, make, model, year):
        """ INIT """
        self.make = make
        self.model  = model
        self.year = year
        self.odometer = 0
        self.gastank = 0
    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return(long_name.title())
    
    def read_odometer(self):
        print(f"{self.year} {self.make} {self.model} has {self.odometer} miles")

    def update_odometer(self, miles):
        if miles <= self.odometer:
            print("Can roll back odometer!")
        else:
            self.odometer = miles
    
    def add_miles(self, miles):
        if miles < 0:
            print("Incorrect Miles")
        else:
            self.odometer += miles

    def fill_gas_tank(self, gallons):
        if gallons < 0:
            print("Enter Valid amount of gas in gallons")
        else:
            self.gastank += gallons
    
    def describe_gas(self):
        print(f"{self.year} {self.make} {self.model} has {self.gastank} gallons")


class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery(50)

    def fill_gas_tank(self, gallons):
        print(f"Electric doesn't have gas tank")

class Battery():

    def __init__(self, batterySize):
        self.battery = batterySize

    def describe_battery(self):
        print(f"This car has a {self.battery}-kWh Battery")

    
my_new_car = Car('audi', 's4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.describe_gas()
my_new_car.fill_gas_tank(10)
my_new_car.describe_gas()

my_tesla = ElectricCar('tesla', 'model x', 2020)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.describe_gas()
my_tesla.fill_gas_tank(20)
my_tesla.describe_gas()


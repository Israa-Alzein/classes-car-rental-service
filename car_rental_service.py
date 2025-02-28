'''You are building a system for a . The system should manage different types of vehicles and allow customers to rent them.

- Attributes: brand, model, year, rental_price_per_day
- Methods:
display_info(): Prints vehicle details.
calculate_rental_cost(days): Returns the rental cost for a given number of days.(inherits from Vehicle):
Additional attribute: seating_capacity
Override display_info() to include seating capacity. (inherits from Vehicle)
Additional attribute: engine_capacity
Override display_info() to include engine capacity.
Make rental_price_per_day a private attribute.
Provide a setter and getter method for rental_price_per_day.
Create a function show_vehicle_info(vehicle) that takes a Vehicle object and calls display_info(), demonstrating polymorphism.
Create instances of Car and Bike with sample data.
Display their details using display_info().
Calculate rental costs for a given number of days.
Modify rental prices using setter methods and display the updated price.
Expected Output:
Car: Toyota Corolla, Year: 2020, Seats: 5, Rental Price: $50/day
Bike: Yamaha R1, Year: 2019, Engine: 998cc, Rental Price: $30/day

Rental cost for Toyota Corolla for 3 days: $150
Rental cost for Yamaha R1 for 5 days: $150

Updated rental price for Toyota Corolla: $55/day'''


class Vehicle:
    def __init__(self, brand, model, year, rental_price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.__rental_price_per_day = rental_price_per_day  #making rental_price_per_day private 

    # getter for rental_price_per_day
    @property       
    def rental_price_per_day(self):
        return self.__rental_price_per_day
    
    # setter for rental_price_per_day
    @rental_price_per_day.setter
    def rental_price_per_day(self, rental_price_per_day):
        self.__rental_price_per_day = rental_price_per_day

    def display_info(self):
        print(f"Vehicle: {self.brand} {self.model}, Year: {self.year}, Rental Price: ${self.rental_price_per_day}/day")

    def calculate_rental_cost(self, days):
        rental_cost = self.rental_price_per_day * days
        print(f"Rental cost for {self.brand} {self.model} for {days} days: ${rental_cost}")
        return rental_cost


class Car(Vehicle):
    def __init__(self, brand, model, year, rental_price_per_day, seating_capacity):
        super().__init__(brand, model, year, rental_price_per_day)  
        self.seating_capacity = seating_capacity

    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}, Seats: {self.seating_capacity} ,Rental Price: ${self.rental_price_per_day}/day")

    def calculate_rental_cost(self, days):
        return super().calculate_rental_cost(days)


class Bike(Vehicle):
    def __init__(self, brand, model, year, rental_price_per_day, engine_capacity):
        super().__init__(brand, model, year, rental_price_per_day)
        self.engine_capacity = engine_capacity

    def display_info(self):
        print(f"Bike: {self.brand} {self.model}, Year: {self.year}, Engine: {self.engine_capacity} ,Rental Price: ${self.rental_price_per_day}/day")

    def calculate_rental_cost(self, days):
        return super().calculate_rental_cost(days)



def prompt():
    print()
    print("=============== Bob's Car Rental Service =================")
    print("Select from the menu below:")
    print("1 ==> To create a new car")
    print("2 ==> To create a new bike")
    print("3 ==> To view car info")
    print("4 ==> To view bike info")
    print("5 ==> To calculate the total rent cost of car for selected number of days")
    print("6 ==> To calculate the total rent cost of bike for selected number of days")
    print("7 ==> To update the cost per day of the car")
    print("8 ==> To update the cost per day of the bike")
    print("9 ==> To exit")

    action = int(input("Choice: "))
    print("==========================================================")
    print()

    return action

def createCar():
    brand = input("Enter the car brand: ")
    model = input("Enter the car model: ")
    year = int(input("Enter the year of the car: "))
    rental_price_per_day = float(input("Enter the rent price of the car per day: "))
    seating_capacity = int(input("Enter the seating capacity of the car: "))
    car = Car(brand, model, year, rental_price_per_day, seating_capacity)
    return car

def createBike():
    brand = input("Enter the bike brand: ")
    model = input("Enter the bike model: ")
    year = int(input("Enter the year of the bike: "))
    rental_price_per_day = float(input("Enter the rent price of the bike per day: "))
    engine_capacity = input("Enter the bike's engine capacty: ")
    bike = Bike(brand, model, year, rental_price_per_day, engine_capacity)
    return bike

def show_vehicle_info(vehicle):
    vehicle.display_info()

def calculate_rent_cost(vehicle):
    days = int(input("For how many days you want to rent the vehicle? : "))
    vehicle.calculate_rental_cost(days)

def update_cost_per_day(vehicle):
    new_cost = float(input("Enter the new cost: "))
    vehicle.rental_price_per_day = new_cost
    print(f"Updated rental price for {vehicle.brand} {vehicle.model}: ${vehicle.rental_price_per_day}/day")


# ========= Main Program ==========


action = 0
previousAction = None
car = None
bike = None

while action != 9:
    if previousAction != None:
        action = previousAction
        previousAction = None
        print(f"Doing action {action} from previous iteration")
    else:
        action = prompt()

    if car == None and action != 1 and action != 9 and (action == 3 or action == 5 or action == 7):
        print("Create a car first:")
        previousAction = action
        action = 1
    elif bike == None and action != 2 and action != 9 and (action == 4 or action == 6 or action == 8):
        print("Create a bike first:")
        previousAction = action
        action = 2

    if action == 1:
        car = createCar()
        print()
    elif action == 2:
        bike = createBike()
        print()
    elif action == 3:
        show_vehicle_info(car)  
        print()
    elif action == 4:
        show_vehicle_info(bike)
        print()
    elif action == 5:
        calculate_rent_cost(car)
        print()
    elif action == 6:
        calculate_rent_cost(bike)
    elif action == 7:
        update_cost_per_day(car)
    elif action == 8:
        update_cost_per_day(bike)
    elif action == 9:
        print("Program Exit")

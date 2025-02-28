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
        self.rental_price_per_day = rental_price_per_day

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

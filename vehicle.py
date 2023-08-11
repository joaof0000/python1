class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.running = False  # Initialize running attribute to False by default
        
    def start(self):
        self.running = True
        print("running...")
        
    def stop(self):
        self.running = False
        print("stopped...")
        
    def __str__(self):
        return f"Vehicle is a {self.make} model {self.model}"

# Instantiate the class and assign to the variable car
car = Vehicle("Toyota", "Camry")

print(car)  # Output: Vehicle is a Toyota model Camry

car.start()  # Output: running...
print(car.running)  # Output: True

car.stop()  # Output: stopped...
print(car.running)  # Output: False



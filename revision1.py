class Car:
    def __init__(self, brand, speed):
        # Attributes: data stored inside the object
        self.brand = brand 
        self.speed = speed

# Method: An action that can manipulate the object's data
    def accelerate(self, amount):
        self.speed += amount

# Create the object (an instance of the Car class)
# Python allocates memory for this object and its attributes

my_car = Car('Toyota', 60)

# Access the object's attributes(its stored data)
print(my_car.brand)
print(my_car.speed)

my_car.accelerate(20)
print(my_car.speed)
    
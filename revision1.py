
# control structures: simple food ordering app
restaurant_open = True

# Outer loop: keep the ordering process running while the restaurant is open
while restaurant_open:
    payment = input('Did the payment succeed? (yes/no:)')

    if payment == 'yes':
        print('order successful, preparing your order')

# If the payment was anything other than 'yes'
    else: 
        print('payment failed')


    while True: # Inner loop: keep asking about the restaurant until we get a valid ans yes/no
        open_status = input('is the restaurant open? (yes/no):')

        if open_status == 'no':
            print('restaurant closed, bye')
            restaurant_open = False # Change the variable to False so the outer loop can stop
            break # Exit the inner loop
        elif open_status == 'yes':
            print('Retrying order')
            break # Exit the inner loop and return to the outer loop
        else:
            print('Enter yes/no:') # Inner loop repeats automatically

    if not restaurant_open: # if the restaurant is closed, exit the outer loop too
            break



# if, elif, else

# score= 85

# if score >= 90:
#     print('Grade A')
# elif score >=80:
#     print('Grade B') # Executes
# else:
#     print('Grace C')

# day_of_the_week = 'Sunday'

# if day_of_the_week == 'Monday':
#     print("It\'s Monday today!")
# elif day_of_the_week == 'Tuesday':
#     print('Today is Tuesday')
# else:
#     print('Wrong day of the week')


# Match 

# day = 2

# match day:
#     case 1:
#         print('Monday')
#     case 2:
#         print('Tuesday')
#     case _:
#         print('Not a correct day of the week!')








# # objects, methods, attributes
# class Car:
#     def __init__(self, brand, speed):
#         # Attributes: data stored inside the object
#         self.brand = brand 
#         self.speed = speed

# # Method: An action that can manipulate the object's data
#     def accelerate(self, amount):
#         self.speed += amount

# # Create the object (an instance of the Car class)
# # Python allocates memory for this object and its attributes

# my_car = Car('Toyota', 60)

# # Access the object's attributes(its stored data)
# print(my_car.brand)
# print(my_car.speed)

# my_car.accelerate(20)
# print(my_car.speed)
    
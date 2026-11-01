
# control structures: simple food ordering app
# restaurant_open = True

# # Outer loop: keep the ordering process running while the restaurant is open
# while restaurant_open:
#     payment = input('Did the payment succeed? (yes/no:)')

#     if payment == 'yes':
#         print('order successful, preparing your order')

# # If the payment was anything other than 'yes'
#     else: 
#         print('payment failed')


#     while True: # Inner loop: keep asking about the restaurant until we get a valid ans yes/no
#         open_status = input('is the restaurant open? (yes/no):')

#         if open_status == 'no':
#             print('restaurant closed, bye')
#             restaurant_open = False # Change the variable to False so the outer loop can stop
#             break # Exit the inner loop
#         elif open_status == 'yes':
#             print('Retrying order')
#             break # Exit the inner loop and return to the outer loop
#         else:
#             print('Enter yes/no:') # Inner loop repeats automatically

# Control flow statements
# Conditional statements  # 1. if, elif, else

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


# 2. Repetition structures(loops)

# for i in range(3):
#     print(f'iteration {i}')

# count = 0
# while count <3:
#     print(f'count is {count}')
#     count +=1

# Getting an index from a list
# names = ['Ann', 'Tom', 'Yu']
# for i in range(len(names)):
#     print(i, names[i])

# for i, name in enumerate(names):
#     print(i, name)

# # 3. Control modifiers # break, continue, pass

# for num in range(1, 6):
#     if num == 3:
#         continue
#     if num == 5:
#         break
#     print(num)




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


# Call the object's METHOD (an action)
# The method changes the data stored in the object

# my_car.accelerate(20)
# print(my_car.speed)
    


# name = 'Mary'
# age = 10

# print(f'My name is {name} and I am {age} years old.')


# x = 10
# if  x == 10:
#     print("Hello")

# fruits = ['apple', 'banana', 'guava']

# Refactor with enumerate function
# for fruit in enumerate(fruits):
#     print(fruit)

# fruits = ['apple', 'guava', 'cherry']
# i = 0

# for fruit in fruits:
#     print(i, fruit)
#     i += 1

# for i in range(5):
#     print('Hello')

# for i in range(0, 7):
#     if i % 2 == 0:
#         print(f'{i} is even')
#     else:
#         print(f'{i} is odd')

# Refactor with a ternary expression

# for i in range(0, 7):
# #     print(f"{i} is {'even' if i % 2 == 0 else 'odd'}")
# # refine further with ternary expression
#       print(f"{i} is {'odd' if i % 2 else 'even'}")

# Positional arguments # Display total
# def calculate_total(price, quantity):
#     total = price * quantity
#     print('Total amount:', total)

# calculate_total(10, 10)

# def student(name, marks):
#     print(name, marks)

# student('Faith', 98)

# Keyword argument
# student(name='Faith, marks=90)

# Same function with return

# def calculate_total(price, quantity):
#     total = price * quantity
#     return total

# result = calculate_total(10, 10)
# print(result)
# print(result + 20)

# Store the returned value in variable

# def add_numbers():
#     return 10 + 10

# result = add_numbers()
# print(result + 10)


# Calling a function multiple times
# def add_numbers():
#     return 10 + 10

# add_numbers()
# print(add_numbers() + 20)
# print(add_numbers() + 5)

# # Reusing a variable in another function
# def add_numbers():
#     return 10 + 10

# result = add_numbers()

# def multiply_numbers():
#     return result * 5
# print(multiply_numbers())

# Reusing the function directly in another function(calling a function inside another function)
# Function composition # Nested function call
# def add_numbers():
#     return 10 + 10

# def multiply_numbers():
#     return add_numbers() * 5

# print(multiply_numbers())

# # Passing one function's result as an argument to another function

# def add_numbers():
#     return 10 + 10

# def multiply_numbers(number):
#     return number * 5

# result = multiply_numbers(add_numbers())
# print(result)


# def add_numbers(a, b):
#     return a + b

# def multiply_numbers(number, multiplier):
#     return number * multiplier

# print(multiply_numbers(add_numbers(10, 10), 10)) # becomes multiply_numbers(20, 5)


# Hardcoded values vs flexible functions

# def add_numbers():
#     return 10 + 10 # will always add 10 + 10

# def multiply_numbers(number):
#     return number * 5 # The multiplier will always be 5

# result = multiply_numbers(add_numbers())
# print(result)

# print(multiply_numbers(10))
# print(multiply_numbers(15))

# Second approach: Passing arguments into functions

# def add_numbers(a, b):
#     return a + b

# def multiply_numbers(number, multiplier):
#     return number * multiplier

# print(multiply_numbers(add_numbers(10, 10), 5))
# print(multiply_numbers(add_numbers(5, 5), 20))

# Optimization

# def add(num1, num2):
#     sum = num1 + num2
#     return sum

# first_result = add(10, 10)
# print(first_result)
# total = add(first_result, 20)
# print(total)

# Same - nested function call
# def add(num1, num2):
#     return num1 + num2

# total = print(add(add(10, 10), 20))


# Nested function

# def outer_function():

#     def add_numbers():
#         return 10 + 10

#     return add_numbers()

# outer_function()
# print(outer_function())

# def outer_function():
#     def inner_function():
#         return 100

#     return inner_function()

# print(outer_function())


# Advanced Functions
# 1. Callbacks

def my_callback(text):
    print('Callback says:' , text)

def process_data(callback_func):
    print('Processing task...')
    callback_func('Hello from inside!')

# Pass the function as an argument

process_data(my_callback)












# Practice: Functions

# Basic function definition
def greet():
    print("Hello, World!")

greet()

# Function with parameter
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")

# Positional arguments
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet("hamster", "Harry")

# Keyword arguments
describe_pet(pet_name="Harry", animal_type="hamster")

# Default arguments
def greet(name, country="USA"):
    print(f"{name} is from {country}")

greet("John")
greet("Sara", "Italy")

# Good practice - mutable default argument
def add_item(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

print(add_item("apple"))
print(add_item("banana"))

# Return statement
def square(number):
    return number * number

result = square(4)
print(result)

# Returning multiple values
def get_stats(numbers):
    return min(numbers), max(numbers)

low, high = get_stats([10, 50, 20])
print(low)
print(high)

# Global keyword
x = 10

def modify_global():
    global x
    x = 20

modify_global()
print(x)

# *args - arbitrary positional arguments
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))

# **kwargs - arbitrary keyword arguments
def print_data(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_data(name="Luke", age=30)

# Docstrings
def add(a, b):
    """
    Adds two numbers and returns the result.
    
    Parameters:
    a (int): First number
    b (int): Second number
    """
    return a + b

print(add(5, 3))

# Type hinting
def greeting(name: str) -> str:
    return "Hello " + name

print(greeting("John"))

# Lambda function
add_lambda = lambda x, y: x + y
print(add_lambda(5, 3))

# Lambda with map
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)

# Recursion
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)

print(factorial(5))

# Decorator
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

say_whee()

# Generator with yield
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

counter = count_up_to(5)
print(next(counter))
print(next(counter))
print(next(counter))

# Functions

## The Basics (Foundations)

To define a function, use the `def` keyword.

```python
def greet():
    # The body of the function must be indented
    print("Hello, World!")

# Calling the function
greet() 
# Output: Hello, World!
```

**Key Rules:**

  * **`def`**: Keywords that starts the function definition.
  * **Function Name**: Should use `snake_case` (lowercase with underscores).
  * **Parentheses `()`**: Can hold parameters (inputs).
  * **Colon `:`**: Marks the end of the header.
  * **Indentation**: Python relies on indentation (usually 4 spaces) to know what code belongs inside the function.

## Part 2: Parameters and Arguments (Inputs)

Information can be passed into functions as arguments.

### Parameters vs. Arguments

  * **Parameter**: The variable listed inside the parentheses in the function definition.
  * **Argument**: The value that is sent to the function when it is called.

```python
def say_hello(name): # 'name' is the parameter
    print(f"Hello, {name}!")

say_hello("Alice")   # "Alice" is the argument
```

### Positional Arguments

Arguments must be passed in the correct order.

```python
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet("hamster", "Harry") 
# Output: I have a hamster named Harry.
```

### Keyword Arguments

You can ignore the order if you specify the parameter names.

```python
describe_pet(pet_name="Harry", animal_type="hamster")
# Output is the same, order doesn't matter here.
```

### Default Arguments

You can assign a default value to a parameter. If the caller doesn't provide a value, the default is used.

```python
def greet(name, country="USA"):
    print(f"{name} is from {country}")

greet("John")           # Uses default country="USA"
greet("Sara", "Italy")  # Overwrites default with "Italy"
```

**⚠️ The Mutable Default Argument Trap:**
Never use a mutable object (like a list) as a default argument.

```python
# BAD PRACTICE
def add_item(item, my_list=[]): 
    my_list.append(item)
    return my_list

# GOOD PRACTICE
def add_item(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list
```

## Return Values (Outputs)

A function doesn't just print things; it often sends data back to the place where it was called using `return`.

### The `return` statement

```python
def square(number):
    return number * number

result = square(4) # result now holds the value 16
print(result)
```

*Note: If a function has no `return` statement, it implicitly returns `None`.*

### Returning Multiple Values

Python allows returning multiple values, which are returned as a **Tuple**.

```python
def get_stats(numbers):
    return min(numbers), max(numbers)

low, high = get_stats([10, 50, 20])
print(low)  # 10
print(high) # 50
```

## Scope and Lifetime

Variables created inside a function are not visible outside it. This is called **Scope**.

### The LEGB Rule

Python looks for variables in this order:

1.  **L**ocal (Inside the current function)
2.  **E**nclosing (Inside enclosing functions - for nested functions)
3.  **G**lobal (Defined at the top level of the script)
4.  **B**uilt-in (Python keywords like `print`, `len`)

### The `global` Keyword

To modify a global variable *inside* a function, you must use the `global` keyword.

```python
x = 10 # Global

def modify_global():
    global x
    x = 20 # Modifies the global x, doesn't create a new local x

modify_global()
print(x) # Output: 20
```

## Flexible Arguments (`*args` and `**kwargs`)

Sometimes you don't know how many arguments a user will pass.

### `*args` (Arbitrary Positional Arguments)

Collects extra positional arguments into a **Tuple**.

```python
def sum_all(*args):
    # args becomes (1, 2, 3, 4)
    return sum(args)

print(sum_all(1, 2, 3, 4)) # Output: 10
```

### `**kwargs` (Arbitrary Keyword Arguments)

Collects extra keyword arguments into a **Dictionary**.

```python
def print_data(**kwargs):
    # kwargs becomes {'name': 'Luke', 'age': 30}
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_data(name="Luke", age=30)
```

## Part 6: Modern Python Features

### Docstrings

Documentation strings explain what the function does.

```python
def add(a, b):
    """
    Adds two numbers and returns the result.
    
    Parameters:
    a (int): First number
    b (int): Second number
    """
    return a + b

# You can access this via help(add)
```

### Type Hinting

You can specify the expected types of arguments and return values. Python doesn't enforce this (it won't crash if you break it), but it helps IDEs catch errors.

```python
def greeting(name: str) -> str:
    return "Hello " + name
```

## Complex & Advanced Features

### Lambda Functions (Anonymous Functions)

Small, one-line functions that have no name.
**Syntax:** `lambda arguments : expression`

```python
# Standard function
def add(x, y):
    return x + y

# Equivalent Lambda
add_lambda = lambda x, y : x + y

print(add_lambda(5, 3)) # 8
```

*Common Use Case:* Used inside higher-order functions like `map`, `filter`, or `sort`.

### Recursion

A function that calls itself. It must have a **Base Case** to stop the loop.

```python
def factorial(x):
    if x == 1: # Base Case
        return 1
    else:
        return (x * factorial(x-1)) # Recursive call

print(factorial(5)) # 120
```

### Decorators (Wrappers)

Decorators allow you to modify the behavior of a function without changing its code. They are functions that take another function as an argument.

```python
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
# Output:
# Something is happening before the function is called.
# Whee!
# Something is happening after the function is called.
```

### Generators (`yield`)

Standard functions use `return` to send back a value and terminate. Generators use `yield` to produce a sequence of values over time, pausing after each one. This saves memory.

```python
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

counter = count_up_to(5)
print(next(counter)) # 1
print(next(counter)) # 2
```
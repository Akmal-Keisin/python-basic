# Practice: Modules - Module File

# Module variables
pi = 3.14159

# Module functions
def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        return "Cannot divide by zero"
    return a / b

# This block only runs when this file is executed directly
if __name__ == "__main__":
    print("Testing my_math module...")
    print(f"add(5, 3) = {add(5, 3)}")
    print(f"subtract(10, 4) = {subtract(10, 4)}")
    print(f"multiply(6, 7) = {multiply(6, 7)}")
    print(f"divide(20, 5) = {divide(20, 5)}")
    print(f"pi = {pi}")

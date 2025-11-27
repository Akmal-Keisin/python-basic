# Practice: Try...Except (Exception Handling)

print("=== Basic Try-Except ===\n")

# Simple exception handling
try:
    numerator = 10
    denominator = 0
    result = numerator / denominator
    print(result)
except:
    print("Oops! You cannot divide by zero.")
print()

# Getting error details
try:
    number = int("Hello World")
except ValueError as e:
    print(f"A specific error occurred: {e}")
print()


print("\n=== Catching Specific Exceptions ===\n")

# Multiple except blocks
try:
    file = open("non_existent_file.txt")
    data = 10 / 0
except FileNotFoundError:
    print("Error: File not found.")
except ZeroDivisionError:
    print("Error: You divided by zero.")
print()

# Grouping exceptions
try:
    result = 10 / 0
except (ZeroDivisionError, ValueError, TypeError) as e:
    print(f"Something went wrong with the math or types: {e}")
print()


print("\n=== The Complete Workflow (else & finally) ===\n")

def read_file_demo(filename):
    """Demonstrates try-except-else-finally structure"""
    f = None
    try:
        f = open(filename, 'r')
        print(f"Opened {filename}")
    except FileNotFoundError:
        print(f"File '{filename}' doesn't exist!")
    else:
        # This runs only if no exception occurred
        content = f.read()
        print(f"Read successful: {len(content)} characters")
    finally:
        # This always runs
        print("Cleanup: Closing operations...")
        if f:
            f.close()
            print("File closed.")

# Test with non-existent file
read_file_demo("non_existent.txt")
print()


print("\n=== Raising Exceptions ===\n")

def set_age(age):
    """Manually raise an exception for invalid input"""
    if age < 0:
        raise ValueError("Age cannot be negative!")
    print(f"Age set to {age}")

try:
    set_age(-5)
except ValueError as err:
    print(f"Error: {err}")
print()

# Valid age
try:
    set_age(25)
except ValueError as err:
    print(f"Error: {err}")
print()


print("\n=== Custom Exceptions ===\n")

class InsufficientFundsError(Exception):
    """Raised when withdrawal is greater than balance"""
    pass

def withdraw(amount, balance):
    """Withdraw money from account"""
    if amount > balance:
        raise InsufficientFundsError(f"Cannot withdraw {amount}. Balance is {balance}")
    return balance - amount

try:
    new_balance = withdraw(100, 50)
    print(f"Withdrawal successful. New balance: {new_balance}")
except InsufficientFundsError as e:
    print(f"Transaction Denied: {e}")
print()

# Successful withdrawal
try:
    new_balance = withdraw(30, 50)
    print(f"Withdrawal successful. New balance: {new_balance}")
except InsufficientFundsError as e:
    print(f"Transaction Denied: {e}")
print()


print("\n=== Exception Chaining ===\n")

try:
    try:
        result = 1 / 0
    except ZeroDivisionError as original_error:
        raise RuntimeError("Database connection failed") from original_error
except RuntimeError as e:
    print(f"Caught: {e}")
    print(f"Original cause: {e.__cause__}")
print()


print("\n=== EAFP vs LBYL ===\n")

import os

# LBYL (Look Before You Leap) - Not Pythonic
print("LBYL approach (Not recommended):")
if os.path.exists("temp_file.txt"):
    os.remove("temp_file.txt")
    print("File removed")
else:
    print("File doesn't exist")
print()

# EAFP (Easier to Ask for Forgiveness than Permission) - Pythonic
print("EAFP approach (Recommended):")
try:
    os.remove("temp_file.txt")
    print("File removed")
except FileNotFoundError:
    print("File doesn't exist (no problem)")
print()


print("\n=== Best Practices ===\n")

# Keep try blocks small
print("1. Keep try blocks small:")
data = [1, 2, 3]
try:
    value = data[10]  # Only the risky line in try
except IndexError:
    print("Index out of range")
    value = None
# Process value here, outside try block
print()

# Don't swallow exceptions silently
print("2. Don't swallow exceptions silently:")
try:
    result = 10 / 2
    print(f"Result: {result}")
except Exception as e:
    # BAD: pass (silently ignores errors)
    # GOOD: Log or handle properly
    print(f"An error occurred: {e}")
print()

# Catch specific exceptions
print("3. Always catch specific exceptions:")
try:
    number = int("123")
    print(f"Converted number: {number}")
except ValueError:  # Specific exception
    print("Could not convert to integer")
# Don't use bare 'except:' - it catches too much!
print()


print("\n=== Practical Example: Safe Division ===\n")

def safe_divide(a, b):
    """Safely divide two numbers with error handling"""
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    except TypeError:
        print("Error: Both arguments must be numbers")
        return None
    else:
        print(f"Division successful: {a} / {b} = {result}")
        return result
    finally:
        print("Division operation completed")

safe_divide(10, 2)
print()
safe_divide(10, 0)
print()
safe_divide(10, "hello")
print()

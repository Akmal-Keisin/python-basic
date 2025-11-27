# Practice: Modules & Packages

print("=== Import Techniques ===\n")

# Method 1: Import the whole module
print("Method 1: Import the whole module")
import my_math
print(f"my_math.pi = {my_math.pi}")
print(f"my_math.add(10, 5) = {my_math.add(10, 5)}")
print()

# Method 2: Import specific items
print("Method 2: Import specific items")
from my_math import pi, subtract
print(f"pi = {pi}")
print(f"subtract(20, 8) = {subtract(20, 8)}")
print()

# Method 3: Import with alias (common in ML/Data Science)
print("Method 3: Import with alias")
import my_math as mm
print(f"mm.multiply(6, 7) = {mm.multiply(6, 7)}")
print(f"mm.divide(50, 10) = {mm.divide(50, 10)}")
print()

# Method 4: Import everything (NOT RECOMMENDED)
# from my_math import *
# This is avoided because it causes namespace pollution

print("\n=== The __name__ Variable ===\n")
print(f"Current file __name__: {__name__}")
print("When you run my_math.py directly, its __name__ will be '__main__'")
print("When imported, my_math's __name__ will be 'my_math'")
print()

print("\n=== Module Search Path ===\n")
import sys
print("Python searches for modules in these locations:")
print("1. Current directory")
print("2. PYTHONPATH environment variable directories")
print("3. Standard library directories")
print("4. Site-packages (third-party packages)")
print(f"\nFirst 3 paths in sys.path:")
for i, path in enumerate(sys.path[:3], 1):
    print(f"{i}. {path}")
print()

print("\n=== Best Practices ===\n")
print("1. Use descriptive, lowercase module names")
print("2. Don't shadow standard library names")
print("3. Sort imports: standard library, third-party, local")
print("4. One import per line")
print("5. Use 'if __name__ == \"__main__\":' for test code")
print()

# Example of proper import ordering
print("Example of proper import order:")
print("""
# Standard library imports
import os
import sys
import math

# Third-party imports
import numpy as np
import pandas as pd

# Local application imports
import my_math
""")

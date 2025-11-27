# Python Modules & Packages

## Understanding Modules

### What is a Module?

Simply put, a **module** is just a file containing Python code (variables, functions, classes) with the `.py` extension.

**Why use them?** To break down large programs into small, manageable, and organized files.

**Analogy:** If a function is a "paragraph", a module is a "chapter" in a book.

### Creating a Module

Imagine you want to create a library for math operations.

**File 1: `my_math.py` (The Module)**

```python
# Save this in a file named my_math.py

pi = 3.14159

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

**File 2: `main.py` (The Script)**
To use the code from `my_math.py`, we use the `import` keyword.

```python
import my_math

print(my_math.pi)          # 3.14159
print(my_math.add(5, 3))   # 8
```

-----

## Import Techniques

There are several ways to import modules. Since you are interested in Machine Learning, you will see specific conventions used frequently (like Method 3).

### Method 1: Import the Whole Module

Best for keeping namespaces clean. You always know where the function came from.

```python
import my_math
my_math.add(10, 5)
```

### Method 2: Import Specific Items (`from ... import`)

Useful if you only need one specific function and don't want to type the module name every time.

```python
from my_math import pi, add

print(pi)   # No need for my_math.pi
print(add(2, 2))
```

### Method 3: Import with an Alias (`as`)

**Standard in Data Science/ML.** This renames the module to something shorter.

```python
import my_math as mm
# Common ML examples: 
# import numpy as np 
# import pandas as pd

print(mm.add(5, 5))
```

### Method 4: Import Everything (`*`)

**Avoid this practice.**

```python
# from my_math import *
```

**Why it's bad:** If `my_math` has a function called `print` and you import it, it will overwrite Python's built-in `print()` function. This causes "Namespace Pollution."


## The `if __name__ == "__main__":` Block

This is one of the most confusing parts for beginners, but it is essential.

When you run a file directly, Python sets a special hidden variable called `__name__` to `"__main__"`. When you import a file, `__name__` is set to the filename.

**Update `my_math.py`:**
```python
def add(a, b):
    return a + b

# This code block only runs if you run THIS file directly.
# It will NOT run if this file is imported by another file.
if __name__ == "__main__":
    print("Testing add function...")
    print(add(2, 2))
```

**Results:**
- **Run `my_math.py`:** You see "Testing add function..."
- **Run `main.py` (which imports `my_math`):** You do **not** see the test print.

-----

## Packages (Organizing Modules)

As your project grows (like a Laravel project with many folders), you need to organize modules into directories. A directory containing modules is called a **package**.

### Directory Structure

To tell Python that a folder is a package, you usually include a special file named `__init__.py`.

```text
my_project/
│
├── main.py
└── ecommerce/           <-- This is a Package
    ├── __init__.py      <-- Markers file
    ├── database.py      <-- Module
    └── payments.py      <-- Module
```

### The `__init__.py` File

**Historically:** It was required to treat a folder as a package.

**Functionality:** The code inside `__init__.py` runs automatically the moment you import the package. It is often used to initialize package-level variables or simplify imports.

### Importing from Packages

In `main.py`, you access the modules using **dot notation**.

```python
# Importing the module
import ecommerce.payments 
ecommerce.payments.process_payment()

# Or using 'from'
from ecommerce.database import connect_db
connect_db()
```

-----

## Advanced Features

### The Module Search Path (`sys.path`)

When you type `import xyz`, where does Python look? It looks in a list of directories defined in `sys.path`.

**The order of search is:**

1. **Current Directory** (Where your script is)
2. **PYTHONPATH** (Environment variable directories)
3. **Standard Library** (Built-in modules)
4. **Site-Packages** (Third-party libraries installed via pip)

### Circular Imports (The "Chicken or Egg" Problem)

This happens when **Module A** imports **Module B**, but **Module B** also imports **Module A**.

**Result:** `ImportError` or `AttributeError`.

**Fix:**
- Refactor code: Move the shared logic to a third **Module C**
- Defer Import: Put the import statement *inside* the function, not at the top of the file

**Example:**
```python
# module_a.py
def func_a():
    from module_b import func_b  # Import inside function prevents circular crash
    func_b()
```

### Absolute vs. Relative Imports

Used when working inside a package.

**Absolute:** `from ecommerce.payments import process` (Preferred, clearest)

**Relative:** `from .payments import process` (The dot `.` means "current package")

-----

## Best Practices

### 1. Naming Conventions
Modules should have short, all-lowercase names. Underscores can be used if it improves readability (e.g., `neural_network.py` is better than `neuralnetwork.py`).

### 2. Don't Shadow Standard Libraries
Never name your file `math.py`, `random.py`, or `email.py`. Python will load *your* file instead of the built-in system library, breaking everything.

### 3. Sort Your Imports
Sort imports in this order (PEP 8 standard):

1. Standard library imports (`os`, `sys`, `math`)
2. Third-party imports (`numpy`, `pandas`, etc.)
3. Local application imports (`my_module`)

### 4. One Import per Line

**Good:**
```python
import os
import sys
```

**Bad:**
```python
import os, sys
```
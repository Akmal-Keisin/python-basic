# Variables

## Understanding Variables

Variables are containers for storing data values. In Python, you don't need to declare a variable's type explicitly - Python figures it out automatically based on the value you assign.

## Creating Variables

### No Declaration Required

Unlike some other programming languages, **Python has no command for declaring a variable**. A variable is created the moment you assign a value to it:

```python
x = 5
y = 2
print(x)  # Output: 5
print(y)  # Output: 2
```

### Dynamic Typing

Variables in Python are **dynamically typed**, meaning they don't need to be declared with a specific type and can even change type after being set:

```python
v = 4       # v is an integer
v = "Sally" # v is now a string
print(v)    # Output: Sally
```

## Type Casting

You can explicitly specify a variable's data type using **casting**:

```python
string = str(3)    # string will be '3'
integer = int(3)   # integer will be 3
float = float(3)   # float will be 3.0
```

## Getting Variable Type

Use the `type()` function to check a variable's data type:

```python
print(type(string))   # <class 'str'>
print(type(integer))  # <class 'int'>
print(type(float))    # <class 'float'>
```

## String Variables

String variables can be declared using either **single quotes** or **double quotes** - they work identically:

```python
x = "John"
x = 'John'  # Same result
```

## Variable Naming Rules

### Valid Variable Names

A variable name must follow these rules:
- Must start with a **letter** or **underscore** (`_`)
- Cannot start with a **number**
- Can only contain **alphanumeric characters** and **underscores** (A-z, 0-9, \_)
- Are **case-sensitive** (age, Age, and AGE are three different variables)
- Cannot be a **Python keyword**

### Legal Examples
```python
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
```

### Illegal Examples
```python
# 2myvar = "John"   # Cannot start with number
# my-var = "John"   # Cannot use hyphens
# my var = "John"   # Cannot use spaces
```

## Multiple Assignment

### Assign Multiple Variables

Python allows assigning values to multiple variables in one line:

```python
x, y, z = "Orange", "Banana", "Cherry"
print(x)  # Orange
print(y)  # Banana
print(z)  # Cherry
```

### Same Value to Multiple Variables

You can assign the same value to multiple variables simultaneously:

```python
x = y = z = "Orange"
print(x)  # Orange
print(y)  # Orange
print(z)  # Orange
```

### Unpacking Collections

Extract values from a list, tuple, etc., into variables. This is called **unpacking**:

```python
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)  # apple
print(y)  # banana
print(z)  # cherry
```

## Variable Scope

### Global Variables

Variables created **outside of a function** are known as **global variables**. They can be used by everyone, both inside and outside functions:

```python
sampleGlobalVarX = "awesome 1"

def myfunc():
    print("Python is " + sampleGlobalVarX)

myfunc()  # Output: Python is awesome 1
```

### Local Variables

If you create a variable **inside a function** with the same name as a global variable, it becomes a **local variable** that only exists within that function. The global variable remains unchanged:

```python
sampleGlobalVarX2 = "awesome 2"

def myfunc2():
    sampleGlobalVarX2 = "fantastic 2"  # This is a local variable
    print("Python is " + sampleGlobalVarX2)

myfunc2()  # Output: Python is fantastic 2
print("Python is " + sampleGlobalVarX2)  # Output: Python is awesome 2
```

### The global Keyword

To create or modify a global variable **inside a function**, use the `global` keyword:

```python
sampleGlobalVarX3 = "awesome 3"

def myfunc():
    global sampleGlobalVarX3
    sampleGlobalVarX3 = "fantastic 3"  # Modifies the global variable

myfunc()
print("Python is " + sampleGlobalVarX3)  # Output: Python is fantastic 3
```

## Key Takeaways

- Variables don't need type declarations
- Variable types can change dynamically
- Follow naming conventions for readable code
- Understand the difference between local and global scope
- Use the `global` keyword when modifying global variables inside functions

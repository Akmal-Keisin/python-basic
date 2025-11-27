# Data Types

## Understanding Python Data Types

Python has a rich set of built-in data types that allow you to store and manipulate different kinds of information. The data type is automatically set when you assign a value to a variable.

## Built-in Data Types

Python includes the following data types organized by category:

### Text Type
- **`str`**: String - for text data

### Numeric Types
- **`int`**: Integer - whole numbers
- **`float`**: Floating-point - decimal numbers
- **`complex`**: Complex numbers - numbers with real and imaginary parts

### Sequence Types
- **`list`**: Ordered, mutable collection
- **`tuple`**: Ordered, immutable collection
- **`range`**: Sequence of numbers

### Mapping Type
- **`dict`**: Dictionary - key-value pairs

### Set Types
- **`set`**: Unordered collection of unique elements
- **`frozenset`**: Immutable version of set

### Boolean Type
- **`bool`**: Boolean - True or False values

### Binary Types
- **`bytes`**: Immutable sequence of bytes
- **`bytearray`**: Mutable sequence of bytes
- **`memoryview`**: Memory view object

### None Type
- **`NoneType`**: Represents the absence of a value

## Checking Data Types

Use the `type()` function to get the data type of any object:

```python
x = 10
print(type(x))  # Output: <class 'int'>
```

## Automatic Type Assignment

In Python, the data type is **automatically set** when you assign a value to a variable:

```python
x = "Hello World"    # str
x = 20               # int
x = 20.5             # float
x = 1j               # complex
x = ["apple", "banana", "cherry"]  # list
x = ("apple", "banana", "cherry")  # tuple
x = range(6)         # range
x = {"name": "John", "age": 36}    # dict
x = {"apple", "banana", "cherry"}  # set
x = frozenset({"apple", "banana", "cherry"})  # frozenset
x = True             # bool
x = b"Hello"         # bytes
x = bytearray(5)     # bytearray
x = memoryview(bytes(5))  # memoryview
x = None             # NoneType
```

## Explicit Type Specification

If you want to **explicitly specify** the data type, use constructor functions:

### Text Constructor
```python
x = str("Hello World")  # str
```

### Numeric Constructors
```python
x = int(20)      # int
x = float(20.5)  # float
x = complex(1j)  # complex
```

### Sequence Constructors
```python
x = list(("apple", "banana", "cherry"))   # list
x = tuple(("apple", "banana", "cherry"))  # tuple
x = range(6)                               # range
```

### Mapping Constructor
```python
x = dict(name="John", age=36)  # dict
```

### Set Constructors
```python
x = set(("apple", "banana", "cherry"))         # set
x = frozenset(("apple", "banana", "cherry"))   # frozenset
```

### Boolean Constructor
```python
x = bool(5)  # bool
```

### Binary Constructors
```python
x = bytes(5)          # bytes
x = bytearray(5)      # bytearray
x = memoryview(bytes(5))  # memoryview
```

## Key Takeaways

- Python automatically determines data types based on assigned values
- Use `type()` to check a variable's data type
- Constructor functions allow explicit type specification
- Understanding data types helps you work more effectively with Python
- Each data type has specific use cases and characteristics

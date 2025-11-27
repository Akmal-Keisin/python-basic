# Casting

## Understanding Casting

**Casting** is the process of converting a value from one data type to another. While Python automatically determines data types, there are times when you need to explicitly specify the type of a variable.

## Why Use Casting?

- Convert user input (strings) to numbers for calculations
- Ensure data is in the correct format for operations
- Handle data from different sources with different types
- Avoid type errors in your code

## Python's Casting Approach

Python is an **object-oriented language** and uses **classes** to define data types, including primitive types. Therefore, casting is done using **constructor functions**:

- **`int()`**: Constructs an integer
- **`float()`**: Constructs a float
- **`str()`**: Constructs a string

## Casting to Integer

The `int()` constructor creates an integer from:

- An **integer literal** (returns the same value)
- A **float literal** (removes all decimals, truncating toward zero)
- A **string literal** (only if the string represents a whole number)

### Examples

```python
intNum1 = int(12)      # From integer: 12
intNum2 = int(12.2)    # From float: 12 (decimals removed)
intNum3 = int("12")    # From string: 12
```

### Important Notes

- Float to int conversion **truncates** (doesn't round)
- String must contain only digits (and optional sign)
- `int("12.5")` will cause an error (decimals in string not allowed)

## Casting to Float

The `float()` constructor creates a float from:

- An **integer literal** (adds `.0`)
- A **float literal** (returns the same value)
- A **string literal** (if it represents a number)

### Examples

```python
floatNum1 = float(8)      # From integer: 8.0
floatNum2 = float(92.2)   # From float: 92.2
floatNum3 = float("23.2") # From string: 23.2
floatNum4 = float("3")    # From string: 3.0
```

### Important Notes

- Integer to float adds decimal point
- String can contain decimals
- Scientific notation in strings is accepted: `float("1e3")` → `1000.0`

## Casting to String

The `str()` constructor creates a string from a **wide variety of data types**:

- String literals
- Integer literals
- Float literals
- Boolean values
- Lists, tuples, dictionaries, etc.

### Examples

```python
stringWord1 = str("s1")  # From string: "s1"
stringWord2 = str(2)     # From integer: "2"
stringWord3 = str(3.0)   # From float: "3.0"
```

### Important Notes

- Converting numbers to strings preserves their representation
- Useful for concatenating numbers with text
- `str(True)` → `"True"`, `str(False)` → `"False"`

## Common Casting Scenarios

### User Input Conversion

User input is always a string, so you often need to cast it:

```python
age = int(input("Enter your age: "))
price = float(input("Enter the price: "))
```

### Number to String for Display

Combine numbers with text:

```python
score = 95
message = "Your score is: " + str(score)
```

### String to Number for Calculations

Process numeric data stored as strings:

```python
num1 = int("42")
num2 = int("8")
result = num1 + num2  # 50
```

## Casting Limitations

### Invalid Conversions

Not all conversions are possible:

```python
# ❌ These will cause errors:
# int("hello")      # ValueError: invalid literal
# int("12.5")       # ValueError: invalid literal  
# float("abc")      # ValueError: could not convert
```

### Data Loss Warning

Some conversions lose data:

```python
x = 3.9
y = int(x)  # y = 3 (lost 0.9)
```

## Key Takeaways

- **Casting** converts values between data types
- Use `int()`, `float()`, and `str()` constructor functions
- `int()` from float truncates (doesn't round)
- String to number conversion requires valid numeric strings
- `str()` works with almost any data type
- Be aware of potential data loss during conversion
- Casting is essential for handling user input and data processing

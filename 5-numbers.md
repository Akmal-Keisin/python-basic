# Numbers

## Numeric Data Types in Python

Python has **three numeric types** for working with numbers:

- **`int`**: Integer numbers
- **`float`**: Floating-point numbers
- **`complex`**: Complex numbers

## Integer (int)

**Integers** are whole numbers, positive or negative, without decimals, and of **unlimited length**.

### Characteristics
- No decimal point
- Can be positive or negative
- No size limit (can be extremely large)

### Examples
```python
int1 = 1
int2 = 35656222554887711
int3 = -3255522
```

## Float

**Float**, or "floating-point number", is a number, positive or negative, containing **one or more decimals**.

### Characteristics
- Contains decimal point
- Can be positive or negative
- Used for precise calculations

### Examples
```python
float1 = 1.10
float2 = 1.0
float3 = -35.59
```

### Scientific Notation

Floats can be expressed in **scientific notation** using an `e` or `E` to indicate the power of 10:

```python
float11 = 35e3      # 35 × 10³ = 35000.0
float12 = 12E4      # 12 × 10⁴ = 120000.0
float13 = -87.7e100 # -87.7 × 10¹⁰⁰
```

## Complex Numbers

**Complex numbers** are written with a `j` as the **imaginary part**. They consist of a real part and an imaginary part.

### Characteristics
- Contains real and imaginary components
- Imaginary part uses `j` suffix
- Used in advanced mathematics and engineering

### Examples
```python
complex1 = 3+5j  # Real: 3, Imaginary: 5j
complex2 = 5j    # Real: 0, Imaginary: 5j
complex3 = -5j   # Real: 0, Imaginary: -5j
```

## Type Conversion

You can **convert between numeric types** using the `int()`, `float()`, and `complex()` functions:

### Conversion Examples
```python
intNum = 1        # int
floatNum = 2.8    # float
complexNum = 1j   # complex

# Convert int to float
a = float(intNum)  # Result: 1.0

# Convert float to int (removes decimals)
b = int(floatNum)  # Result: 2

# Convert int to complex
c = complex(intNum)  # Result: (1+0j)
```

### Important Note
⚠️ **You cannot convert complex numbers into other number types**

## Random Numbers

Python doesn't have a built-in `random()` function, but it has a **`random` module** for generating random numbers:

### Using the random Module
```python
import random

# Generate random integer from 1 to 9 (10 is excluded)
print(random.randrange(1, 10))
```

### Common random Module Functions
- `random.randrange(start, stop)`: Random integer from range
- `random.randint(a, b)`: Random integer between a and b (inclusive)
- `random.random()`: Random float between 0.0 and 1.0
- `random.choice(sequence)`: Random element from a sequence

## Key Takeaways

- Python supports three numeric types: int, float, and complex
- Integers have unlimited precision
- Floats support scientific notation
- Complex numbers use `j` for the imaginary part
- Type conversion is possible between int, float, and complex (except from complex)
- Use the `random` module for generating random numbers

# Operators

## Understanding Operators

Operators are special symbols that perform operations on variables and values. Python includes several categories of operators for different purposes.

## Arithmetic Operators

Arithmetic operators are used to perform **mathematical operations** on numeric values.

| Operator | Name           | Description                                | Example             |
| -------- | -------------- | ------------------------------------------ | ------------------- |
| `+`      | Addition       | Adds two operands                          | `10 + 3 = 13`       |
| `-`      | Subtraction    | Subtracts right operand from left          | `10 - 3 = 7`        |
| `*`      | Multiplication | Multiplies two operands                    | `10 * 3 = 30`       |
| `/`      | Division       | Divides left by right (float result)       | `10 / 3 = 3.333...` |
| `//`     | Floor Division | Divides and rounds down to nearest integer | `10 // 3 = 3`       |
| `%`      | Modulus        | Returns remainder of division              | `10 % 3 = 1`        |
| `**`     | Exponentiation | Raises left to power of right              | `10 ** 3 = 1000`    |

### Examples
```python
a = 10
b = 3

print("Addition:", a + b)          # 13
print("Subtraction:", a - b)       # 7
print("Multiplication:", a * b)    # 30
print("Division:", a / b)          # 3.333...
print("Floor Division:", a // b)   # 3
print("Modulus:", a % b)           # 1
print("Exponentiation:", a ** b)   # 1000
```

## Comparison Operators

Comparison operators are used to **compare two values**. They return a Boolean result (`True` or `False`).

| Operator | Name                  | Description                          | Example             |
| -------- | --------------------- | ------------------------------------ | ------------------- |
| `==`     | Equal                 | Checks if values are equal           | `10 == 3` → `False` |
| `!=`     | Not Equal             | Checks if values are not equal       | `10 != 3` → `True`  |
| `>`      | Greater Than          | Checks if left is greater than right | `10 > 3` → `True`   |
| `<`      | Less Than             | Checks if left is less than right    | `10 < 3` → `False`  |
| `>=`     | Greater Than or Equal | Checks if left is greater or equal   | `10 >= 3` → `True`  |
| `<=`     | Less Than or Equal    | Checks if left is less or equal      | `10 <= 3` → `False` |

### Examples
```python
a = 10
b = 3

print("Equal:", a == b)                    # False
print("Not Equal:", a != b)                # True
print("Greater Than:", a > b)              # True
print("Less Than:", a < b)                 # False
print("Greater Than or Equal:", a >= b)    # True
print("Less Than or Equal:", a <= b)       # False
```

## Logical Operators

Logical operators are used to **combine conditional statements**.

| Operator | Description                                    | Example   |
| -------- | ---------------------------------------------- | --------- |
| `and`    | Returns True if both statements are true       | `x and y` |
| `or`     | Returns True if at least one statement is true | `x or y`  |
| `not`    | Reverses the result, returns False if true     | `not x`   |

### Examples
```python
x = True
y = False

print("Logical AND:", x and y)  # False
print("Logical OR:", x or y)    # True
print("Logical NOT:", not x)    # False
```

### Truth Table

| x     | y     | x and y | x or y | not x |
| ----- | ----- | ------- | ------ | ----- |
| True  | True  | True    | True   | False |
| True  | False | False   | True   | False |
| False | True  | False   | True   | True  |
| False | False | False   | False  | True  |

## String Operators

Special operators can be used with **strings**:

### Concatenation (`+`)
Joins two strings together:
```python
str1 = "Hello"
str2 = "World"
print(str1 + " " + str2)  # "Hello World"
```

### Repetition (`*`)
Repeats a string multiple times:
```python
print(str1 * 3)  # "HelloHelloHello"
```

### Membership (`in`)
Checks if a character or substring exists in a string:
```python
print('H' in str1)   # True
print('z' in str2)   # False
```

## Key Takeaways

- **Arithmetic operators** perform mathematical calculations
- **Comparison operators** compare values and return boolean results
- **Logical operators** combine multiple conditions
- **String operators** allow concatenation, repetition, and membership testing
- Understanding operators is fundamental to writing effective Python code

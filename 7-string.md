# Strings

## Understanding Strings

Strings in Python are sequences of characters used to store and manipulate text. They are one of the most commonly used data types.

## Creating Strings

### Quotation Marks

Strings can be surrounded by either **single quotation marks** or **double quotation marks** - both work identically:

```python
'hello' == "hello"  # True
```

### Displaying Strings

Use the `print()` function to display strings:

```python
print("Hello World")
print('Hello World')
```

### String Variables

Assign a string to a variable using the variable name, an equal sign, and the string:

```python
stringWord1 = "Hello World"
print(stringWord1)
```

## Multiline Strings

Assign a **multiline string** to a variable using **three quotes** (either `"""` or `'''`):

```python
stringParagraph1 = """
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
"""

# Or with single quotes
stringParagraph2 = '''
Lorem ipsum dolor sit amet,
consectetur adipiscing elit
'''
```

## Strings as Arrays

Strings in Python are **arrays of bytes** representing Unicode characters. However, Python doesn't have a separate character data type - a single character is simply a string of length 1.

### Accessing Characters

Use **square brackets** to access elements:

```python
stringWord1 = "Hello World"
print(stringWord1[2])  # Output: l (index starts at 0)
```

### Looping Through Strings

Loop through the characters using a `for` loop:

```python
for letter in "Hello World":
    print(letter)
```

### String Length

Get the length of a string using the `len()` function:

```python
print(len("Hello World"))  # Output: 11
```

## Checking String Content

### Check if Present (`in`)

Check if a phrase or character is present in a string:

```python
print("Hello" in stringWord1)  # True

if "Hello" in stringWord1:
    print("Found!")
```

### Check if Not Present (`not in`)

Check if a phrase or character is NOT present:

```python
print("Hello" not in stringWord1)  # False

if "Hello" not in stringWord1:
    print("Not Hello")
else:
    print("Hello")
```

## String Slicing

Return a **range of characters** using the slice syntax: `[start:end]`

### Basic Slicing

```python
stringWord1 = "Hello World"
print(stringWord1[2:8])  # Output: llo Wo
```

**Note**: The first character has index 0, and the end index is **not included**.

### Slice From Start

Leave out the start index to begin from the first character:

```python
print(stringWord1[:5])  # Output: Hello
```

### Slice To End

Leave out the end index to go to the end:

```python
print(stringWord1[5:])  # Output:  World
```

### Negative Indexing

Use negative indexes to start from the end:

```python
print(stringWord1[-5:-2])  # Output: Wor
```

## String Methods

Python has many built-in **string methods** for manipulating strings:

### upper()
Returns the string in uppercase:
```python
print(stringWord1.upper())  # HELLO WORLD
```

### lower()
Returns the string in lowercase:
```python
print(stringWord1.lower())  # hello world
```

### strip()
Removes whitespace from beginning or end:
```python
print(stringWord1.strip())
```

### replace()
Replaces a string with another:
```python
print(stringWord1.replace('World', 'Python!'))  # Hello Python!
```

### split()
Splits the string into a list:
```python
print(stringWord1.split(' '))  # ['Hello', 'World']
```

## String Concatenation

### Using the + Operator

Combine two strings using the `+` operator:

```python
print('Hello' + ' ' + 'World')  # Hello World
```

### Combining Strings and Numbers

**You cannot directly combine strings and numbers**:

```python
# ❌ This will cause an error:
# age = 20
# txt = "My name is Keisin, I am " + age
```

## F-Strings (Formatted String Literals)

**F-strings** allow you to embed expressions inside string literals using curly brackets `{}`.

### Basic Usage

Put an `f` before the string literal:

```python
age = 20
txt = f"My name is Keisin, I am {age}"
print(txt)  # My name is Keisin, I am 20
```

### Advanced F-Strings

Placeholders can contain **variables, operations, functions, and modifiers**:

```python
price = 59
txt = f"The price is {price * 1.1} dollars"
```

## Escape Characters

Use **escape characters** to insert characters that are illegal in strings. An escape character is a backslash `\` followed by the character you want to insert.

### Example

Insert a double quote inside a double-quoted string:

```python
print("\"That was amazing.\" Larry told me")
```

### Common Escape Characters

| Code   | Result | Description     |
| ------ | ------ | --------------- |
| `\'`   | '      | Single Quote    |
| `\\`   | \      | Backslash       |
| `\n`   |        | New Line        |
| `\r`   |        | Carriage Return |
| `\t`   |        | Tab             |
| `\b`   |        | Backspace       |
| `\f`   |        | Form Feed       |
| `\ooo` |        | Octal value     |
| `\xhh` |        | Hex value       |

## Key Takeaways

- Strings can use single or double quotes
- Strings are arrays and can be indexed and sliced
- Use `in` and `not in` to check string content
- String methods provide powerful text manipulation
- F-strings allow embedding variables and expressions
- Escape characters handle special characters in strings

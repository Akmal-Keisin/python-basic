# Boolean

## Understanding Booleans

Booleans represent one of two values: **`True`** or **`False`**. They are fundamental to programming logic and decision-making.

## Boolean Values

In programming, you often need to know if an expression is True or False. Python returns Boolean values when you evaluate expressions.

### Comparison Results

When you compare two values, the expression is evaluated and Python returns a Boolean answer:

```python
print(19 > 11)   # True
print(12 == 3)   # False
print(412 < 239) # False
```

## Booleans in Conditionals

Booleans are commonly used in **if statements** to control program flow:

```python
x = 231
y = 112

if x > y:
    print(f"{x} is greater than {y}")
else:
    print(f"{y} is greater than {x}")
```

## The bool() Function

The `bool()` function allows you to **evaluate any value** and returns `True` or `False`:

```python
print(bool(12))            # True
print(bool("Hello World")) # True
```

## Values That Evaluate to True

**Almost any value** is evaluated to `True` if it has some sort of content:

- Any **string** is True, except empty strings
- Any **number** is True, except `0`
- Any **list, tuple, set, or dictionary** is True, except empty ones

### Examples of True Values

```python
print(bool("abc"))                      # True
print(bool(123))                        # True
print(bool(["apple", "cherry", "banana"])) # True
```

## Values That Evaluate to False

Only a few values evaluate to `False`:

- `False` (the boolean value itself)
- `None` (represents absence of value)
- `0` (zero in any numeric type)
- `""` (empty string)
- `()` (empty tuple)
- `[]` (empty list)
- `{}` (empty dictionary)

### Examples of False Values

```python
print(bool(False))  # False
print(bool(None))   # False
print(bool(0))      # False
print(bool(""))     # False
print(bool(()))     # False
print(bool([]))     # False
print(bool({}))     # False
```

## Objects with __len__ Method

Objects made from a class with a `__len__` function that returns `0` or `False` also evaluate to `False`:

```python
class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))  # False
```

## Functions Returning Booleans

Functions can return Boolean values, which is useful for creating reusable conditional logic:

```python
def boolFunction():
    return True

if boolFunction():
    print("The function is True")
else:
    print("The function is False")
```

### Use Cases

- **Validation functions**: Check if input is valid
- **Comparison functions**: Compare complex objects
- **State checkers**: Check if a condition is met

## Key Takeaways

- Booleans have only two values: `True` or `False`
- Comparison operators return Boolean values
- Use `bool()` to evaluate any value as True or False
- Most values with content are True
- Empty values and zero are False
- Functions can return Boolean values for reusable logic
- Booleans are essential for control flow (if statements, loops, etc.)

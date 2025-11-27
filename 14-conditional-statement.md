# Conditional Statement

## If Statement

### The if Keyword
An "if statement" is written by using the `if` keyword.
```python
a = 33
b = 200
if b > a:
  print("b is greater than a")
```

### The elif Keyword
The `elif` keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

The `elif` keyword allows you to check multiple expressions for True and execute a block of code as soon as one of the conditions evaluates to True.
```python
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
```

### The else Keyword
The `else` keyword catches anything which isn't caught by the preceding conditions.

The `else` statement is executed when the if condition (and any elif conditions) evaluate to False.
```python
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
```

### Pass Statement
`if` statements cannot be empty, but if you for some reason have an `if` statement with no content, put in the `pass` statement to avoid getting an error.
```python
a = 33
b = 200

if b > a:
  pass
```
The `pass` statement is a null operation - nothing happens when it executes. It serves as a placeholder.

The `pass` statement is useful in several situations:
- When you're creating code structure but haven't implemented the logic yet
- When a statement is required syntactically but no action is needed
- As a placeholder for future code during development
- In empty functions or classes that you plan to implement later

## Match Statement
Instead of writing many `if..else` statements, you can use the `match` statement.

The `match` statement selects one of many code blocks to be executed.
```
match expression:
  case x:
    code block
  case y:
    code block
  case z:
    code block
```

```python
day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
```

### Default Value
Use the underscore character `_` as the last case value if you want a code block to execute when there are no other matches:
```python
day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")
```

### Combine Values
Use the pipe character `|` as an OR operator in the case evaluation to check for more than one value match in one case:
```python
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")
```
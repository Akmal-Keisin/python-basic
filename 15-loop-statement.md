# Loop Statement

## While Loop
With the `while` loop we can execute a set of statements as long as a condition is true.

**Example:** Print `i` as long as `i` is less than 6:
```python
i = 1
while i < 6:
  print(i)
  i += 1
```

### The break Statement
With the `break` statement we can stop the loop even if the while condition is true:
```python
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
```

### The continue Statement
With the `continue` statement we can stop the current iteration, and continue with the next:
```python
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
```

### The else Statement
With the `else` statement we can run a block of code once when the condition no longer is true.

**Example:** Print a message once the condition is false:
```python
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
```

## For Loop
A `for` loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the `for` keyword in other programming languages, and works more like an iterator method as found in other object-oriented programming languages.

With the `for` loop we can execute a set of statements, once for each item in a list, tuple, set etc.

```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
```

### Looping Through a String
Even strings are iterable objects, they contain a sequence of characters:
```python
for x in "banana":
  print(x)
```

**Note:** `break` and `continue` statements work the same way in `for` loops as they do in `while` loops.

### range() Function
To loop through a set of code a specified number of times, we can use the `range()` function.

The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.	
```python
for x in range(6):
  print(x)
```
**Note:** `range(6)` is not the values of 0 to 6, but the values 0 to 5 (the end value is excluded).

The `range()` function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: `range(2, 6)`, which means values from 2 to 6 (but not including 6):
```python
for x in range(2, 6):
  print(x)
```

The `range()` function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: `range(2, 30, 3)`:
```python
for x in range(2, 30, 3):
  print(x)
```

**Note:** The `else` block works the same way in `for` loops as it does in `while` loops.
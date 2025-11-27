# Tuple

Tuples are used to store multiple items in a single variable.
Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
A tuple is a collection which is ordered and **unchangeable**.
Tuples are written with round brackets.

```python
fruits = ("apple", "banana", "cherry")
print(fruits)
```

## Tuple Items
Tuple items are **ordered, unchangeable, and allow duplicate values**.

Tuple items are **indexed**, the first item has index [0], the second item has index [1] etc.

### Ordered
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

### Unchangeable
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

### Allow Duplicates
Since tuples are indexed, they can have items with the same value:
```python
fruits = ("apple", "banana", "cherry", "apple", "cherry")
print(fruits)
```

## Accessing Tuple Items

### Access Using Index
```python
fruits = ("apple", "banana", "cherry")
print(fruits[1])
```

The rest of accessing tuple items is the same as accessing list items.

## Unpacking Tuples

### Unpacking a Tuple
When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
```python
fruits = ("apple", "banana", "cherry")
```

But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
```python
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
```

### Using Asterisk
If the number of variables is less than the number of values, you can add an `*` to the variable name and the values will be assigned to the variable as a list:
```python
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
```

If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.

```python
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
```
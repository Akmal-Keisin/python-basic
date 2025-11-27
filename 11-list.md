# List

## Understanding List
Lists are used to store multiple items in a single variable.
Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
Lists are created using square brackets:

```python
fruits = ["apple", "banana", "cherry"]
print(fruits)
```

## List Items
List items are **ordered, changeable, and allow duplicate values**.
List items are **indexed**, the first item has index [0], the second item has index [1] etc.

### Ordered
When we say that lists are ordered, it means that **the items have a defined order**, and **that order will not change**.
If you add new items to a list, the new items will be placed at the end of the list.

### Changable
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

### Allow Duplicates
Since lists are indexed, lists can have items with the same value:
```python
fruits = ["apple", "banana", "cherry", "apple", "cherry"]
print(fruits)
```

## Access Item
List items are indexed and you can access them by referring to the index number:
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
```

### Check if item exist
To determine if a specified item is present in a list use the in keyword:
```python
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
```

## Change List Item
To change the value of a specific item, refer to the index number:
```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blackcurrant"
print(fruits)
```
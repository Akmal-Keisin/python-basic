# List

## Understanding Lists
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

### Changeable
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

### Allow Duplicates
Since lists are indexed, lists can have items with the same value:
```python
fruits = ["apple", "banana", "cherry", "apple", "cherry"]
print(fruits)
```

## Accessing Items
List items are indexed and you can access them by referring to the index number:
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
```

### Check if Item Exists
To determine if a specified item is present in a list, use the `in` keyword:
```python
fruits = ["apple", "banana", "cherry"]
if "apple" in fruits:
  print("Yes, 'apple' is in the fruits list")
```

## Changing List Items
To change the value of a specific item, refer to the index number:
```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blackcurrant"
print(fruits)
```

### Change a Range of Item Values
To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:
```python
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
fruits[1:3] = ["blackcurrant", "watermelon"]
print(fruits)
```
If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
```python
fruits = ["apple", "banana", "cherry"]
fruits[1:2] = ["blackcurrant", "watermelon"]
print(fruits)
```

### Inserting Items
To insert a new list item, without replacing any of the existing values, we can use the `insert()` method.

The `insert()` method inserts an item at the specified index:
```python
fruits = ["apple", "banana", "cherry"]
fruits.insert(2, "watermelon")
print(fruits)
```

## Adding Items to List

### Append
To add an item to the end of the list, use the `append()` method:
```python
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)
```

### Extend
To append elements from another list to the current list, use the `extend()` method.
```python
fruits = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
fruits.extend(tropical)
print(fruits)
```

The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
```python
fruitList = ["apple", "banana", "cherry"]
fruitTuple = ("kiwi", "orange")
fruitList.extend(fruitTuple)
print(fruitList)
```

## Removing Items from List

### Using pop() Method
The `pop()` method removes the specified index.
```python
fruits = ["apple", "banana", "cherry"]
fruits.pop(1)
print(fruits)
```

If you do not specify the index, the pop() method removes the last item.
```python
fruits = ["apple", "banana", "cherry"]
fruits.pop()
print(fruits)
```

### Using del Keyword
The `del` keyword also removes the specified index:
```python
fruits = ["apple", "banana", "cherry"]
del fruits[0]
print(fruits)
```

The del keyword can also delete the list completely.
```python
fruits = ["apple", "banana", "cherry"]
del fruits
```

### Clear List
The `clear()` method empties the list.
The list still remains, but it has no content.
```python
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)
```
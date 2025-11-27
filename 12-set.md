# Set

Sets are used to store multiple items in a single variable.
Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
A set is a collection which is unordered, unchangeable*, and unindexed.

```python
sampleSet = {"apple", "banana", "cherry"}
print(sampleSet)
```

**Note:** Sets are unordered, so you cannot be sure in which order the items will appear.

## Set Items
Set items are unordered, unchangeable, and do not allow duplicate values.

### Unordered
Unordered means that the items in a set do not have a defined order.
Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

### Unchangeable
Set items are unchangeable, meaning that we cannot change the items after the set has been created.
Once a set is created, you cannot change its items, but you can remove items and add new items.

### Duplicates Not Allowed
Sets cannot have two items with the same value.
Duplicate value will be ignored.
```python
sampleSet = {"apple", "banana", "cherry", "apple"}
print(sampleSet)
```

Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
```python
sampleSet = {"apple", "banana", "cherry", True, 1, 2}
print(sampleSet)
```

Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:
```python
sampleSet = {"apple", "banana", "cherry", False, True, 0}
print(sampleSet)
```

## Access Items
You cannot access items in a set by referring to an index or a key.
But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

```python
sampleSet = {"apple", "banana", "cherry"}

for x in sampleSet:
  print(x)
```

Check if "banana" is present in the set:
```python
sampleSet = {"apple", "banana", "cherry"}
print("banana" in sampleSet)
```

Check if "banana" is NOT present in the set:
```python
sampleSet = {"apple", "banana", "cherry"}
print("banana" not in sampleSet)
```

## Add Item to Set
Once a set is created, you cannot change its items, but you can add new items.

To add one item to a set use the add() method.
```python
sampleSet = {"apple", "banana", "cherry"}
sampleSet.add("orange")
print(sampleSet)
```

To add items from another set into the current set, use the update() method.
Add elements from tropical into sampleSet:
```python
sampleSet = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

sampleSet.update(tropical)

print(sampleSet)
```

The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

Add elements of a list to at set:
```python
sampleSet = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

sampleSet.update(mylist)

print(sampleSet)
```

## Remove Set Item
To remove an item in a set, use the remove(), or the discard() method.
Remove "banana" by using the remove() method:
```python
sampleSet = {"apple", "banana", "cherry"}
sampleSet.remove("banana")
print(sampleSet)
```

Note: If the item to remove does not exist, remove() will raise an error.

Remove "banana" by using the discard() method:
```python
sampleSet = {"apple", "banana", "cherry"}
sampleSet.discard("banana")
print(sampleSet)
```

Note: If the item to remove does not exist, discard() will NOT raise an error.

You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.

The return value of the pop() method is the removed item.

```python
sampleSet = {"apple", "banana", "cherry"}
x = sampleSet.pop()
print(x)
print(sampleSet)
```
Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

The clear() method empties the set:
```python
sampleSet = {"apple", "banana", "cherry"}
sampleSet.clear()
print(sampleSet)
```

The del keyword will delete the set completely:
```python
sampleSet = {"apple", "banana", "cherry"}
del sampleSet
print(sampleSet)
```

## Frozen Set

`frozenset` is an **immutable version of a set**.

Like sets, it contains unique, unordered, unchangeable elements.
Unlike sets, elements cannot be added or removed from a frozenset.

Use the `frozenset()` constructor to create a frozenset from any iterable.
```python
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
```
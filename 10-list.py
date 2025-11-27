# Practice: List

# Creating a list
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Lists allow duplicates
fruits = ["apple", "banana", "cherry", "apple", "cherry"]
print(fruits)

# Accessing items by index
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

# Check if item exists
fruits = ["apple", "banana", "cherry"]
if "apple" in fruits:
    print("Yes, 'apple' is in the fruits list")

# Change list item
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blackcurrant"
print(fruits)

# Change a range of item values
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
fruits[1:3] = ["blackcurrant", "watermelon"]
print(fruits)

# Insert more items than replaced
fruits = ["apple", "banana", "cherry"]
fruits[1:2] = ["blackcurrant", "watermelon"]
print(fruits)

# Insert item at specific index
fruits = ["apple", "banana", "cherry"]
fruits.insert(2, "watermelon")
print(fruits)

# Append - add item to the end
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

# Extend - append elements from another list
fruits = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
fruits.extend(tropical)
print(fruits)

# Extend with tuple
fruitList = ["apple", "banana", "cherry"]
fruitTuple = ("kiwi", "orange")
fruitList.extend(fruitTuple)
print(fruitList)

# Remove item using pop() - removes specified index
fruits = ["apple", "banana", "cherry"]
fruits.pop(1)
print(fruits)

# pop() without index - removes last item
fruits = ["apple", "banana", "cherry"]
fruits.pop()
print(fruits)

# Remove item using del keyword
fruits = ["apple", "banana", "cherry"]
del fruits[0]
print(fruits)

# Clear list - empties the list
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)

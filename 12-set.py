# Practice: Set

# Creating a set
sampleSet = {"apple", "banana", "cherry"}
print(sampleSet)

# Sets ignore duplicate values
sampleSet = {"apple", "banana", "cherry", "apple"}
print(sampleSet)

# True and 1 are considered duplicates
sampleSet = {"apple", "banana", "cherry", True, 1, 2}
print(sampleSet)

# False and 0 are considered duplicates
sampleSet = {"apple", "banana", "cherry", False, True, 0}
print(sampleSet)

# Loop through set items
sampleSet = {"apple", "banana", "cherry"}
for x in sampleSet:
    print(x)

# Check if item is present
sampleSet = {"apple", "banana", "cherry"}
print("banana" in sampleSet)

# Check if item is NOT present
sampleSet = {"apple", "banana", "cherry"}
print("banana" not in sampleSet)

# Add one item to set
sampleSet = {"apple", "banana", "cherry"}
sampleSet.add("orange")
print(sampleSet)

# Update set with another set
sampleSet = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
sampleSet.update(tropical)
print(sampleSet)

# Update set with a list
sampleSet = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
sampleSet.update(mylist)
print(sampleSet)

# Remove item using remove()
sampleSet = {"apple", "banana", "cherry"}
sampleSet.remove("banana")
print(sampleSet)

# Remove item using discard()
sampleSet = {"apple", "banana", "cherry"}
sampleSet.discard("banana")
print(sampleSet)

# Remove random item using pop()
sampleSet = {"apple", "banana", "cherry"}
x = sampleSet.pop()
print(x)
print(sampleSet)

# Clear set - empties the set
sampleSet = {"apple", "banana", "cherry"}
sampleSet.clear()
print(sampleSet)

# Create a frozenset
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

# Python knows a number of compound data types, used to group together other values. 
# The most versatile is the list, which can be written as a list of comma-separated values (items) between square brackets. 
# Lists might contain items of different types, but usually the items all have the same 
numbers = [1, 2, 4, 28, 123]
print(numbers)

# Like strings (and all other built-in sequence types), lists can be indexed and sliced:
print(numbers[0]) # indexing returns the item
print(numbers[-1])
print(numbers[-4:]) # slicing returns a new list

# Lists also support operations like concatenation:
print(numbers + [12, 312, 234, 12, 312])

# Unlike strings, which are immutable, lists are a mutable type, i.e. 
# It is possible to change their content:
testNumbers = [1, 2, 3, 4, 5]
replaceNumber = 9 ** 2

testNumbers[0] = replaceNumber
print(testNumbers)

# You can also add new items at the end of the list, by using the list.append() method
testNumbers.append(123)
testNumbers.append(20 ** 2)
print(testNumbers)

# Simple assignment in Python never copies data. 
# When you assign a list to a variable, the variable refers to the existing list. 
# Any changes you make to the list through one variable will be seen through all other variables that refer to it.:
rgb = ["Red", "Green", "Blue"]
rgba = rgb
print(id(rgb) == id(rgba) ) # they reference the same object

rgba.append('Alph')
print(rgb)

# All slice operations return a new list containing the requested elements. 
# This means that the following slice returns a shallow copy of the list:
correct_rgba = rgba[:] # this is not refer to rgba
correct_rgba[-1] = "Alpha"
print(correct_rgba)
print(rgba)

# Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)

letters[2:5] = ['C', 'D', 'E']
print(letters)

letters[:] = []
print(letters)

# The built-in function len() also applies to lists:
letters = ['a', 'b', 'c', 'd']
print(len(letters))

# It is possible to nest lists (create lists containing other lists), for example:
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(id(x[0]) == id(a))
print(x[0][1])
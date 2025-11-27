# Practice: Tuple

# Creating a tuple
fruits = ("apple", "banana", "cherry")
print(fruits)

# Tuples allow duplicates
fruits = ("apple", "banana", "cherry", "apple", "cherry")
print(fruits)

# Accessing tuple items by index
fruits = ("apple", "banana", "cherry")
print(fruits[1])

# Unpacking a tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# Using asterisk - remaining values as list
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

# Asterisk in middle position
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

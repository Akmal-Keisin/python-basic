# Practice: Loop Statement

# While loop - basic
i = 1
while i < 6:
    print(i)
    i += 1

# While loop with break
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# While loop with continue
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# While loop with else
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

# For loop - iterating over list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# For loop - iterating through string
for x in "banana":
    print(x)

# For loop with range - default start from 0
for x in range(6):
    print(x)

# For loop with range - specify start and end
for x in range(2, 6):
    print(x)

# For loop with range - specify increment
for x in range(2, 30, 3):
    print(x)

# For loop with break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

# For loop with continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# For loop with else
for x in range(6):
    print(x)
else:
    print("Finally finished!")

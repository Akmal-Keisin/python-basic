# Practice: Variables

# Creating variables (no declaration needed)
x = 5
y = 2
print(x)
print(y)

# Dynamic typing - variables can change type
v = 4
v = "Sally"
print(v)

# Casting - explicitly specify data type
string = str(3)
integer = int(3)
float = float(3)

# Check variable types
print(type(string))
print(type(integer))
print(type(float))

# String variables with quotes
x = "John"
x = 'John'  # Same result

# Multiple assignment
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# Same value to multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpacking collections
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Global variables - can be used everywhere
sampleGlobalVarX = "awesome 1"

def myfunc():
    print("Python is " + sampleGlobalVarX)

myfunc()

# Local vs Global variables
sampleGlobalVarX2 = "awesome 2"

def myfunc2():
    sampleGlobalVarX2 = "fantastic 2"  # Local variable
    print("Python is " + sampleGlobalVarX2)

myfunc2()
print("Python is " + sampleGlobalVarX2)

# Using global keyword to modify global variable inside function
sampleGlobalVarX3 = "awesome 3"

def myfunc3():
    global sampleGlobalVarX3
    sampleGlobalVarX3 = "fantastic 3"

myfunc3()
print("Python is " + sampleGlobalVarX3)
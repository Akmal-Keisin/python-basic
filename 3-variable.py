# Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.

# x = 5
# y = 2

# print(x)
# print(y)

# Variables do not need to be declared with any particular type, and can even change type after they have been set.

# v = 4 # x is of type int
# v = "Sally" # x is now of type str
# print(v)

# If you want to specify the data type of a variable, this can be done with casting.

# string = str(3) # x will be '3'
# integer = int(3) # y will be 3
# float = float(3) # z will be 3.0

# You can get the data type of a variable with the type() function.

# print(type(string))
# print(type(integer))
# print(type(float))

# String variables can be declared either by using single or double quotes:

# x = "John"
# # is the same as
# x = 'John'

# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
    # A variable name must start with a letter or the underscore character
    # A variable name cannot start with a number
    # A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    # Variable names are case-sensitive (age, Age and AGE are three different variables)
    # A variable name cannot be any of the Python keywords.

# Legal variable name:
# myvar = "John"
# my_var = "John"
# _my_var = "John"
# myVar = "John"
# MYVAR = "John"
# myvar2 = "John"

# Illegal variable name: 
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# Python allows you to assign values to multiple variables in one line:
# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)

# And you can assign the same value to multiple variables in one line:
# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)

# If you have a collection of values in a list, tuple etc. 
# Python allows you to extract the values into variables. 
# This is called unpacking.

# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)

# Variables that are created outside of a function (as in all of the examples above) are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.
# x = "awesome"

# def myfunc():
#   print("Python is " + x)

# myfunc()

# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. 
# The global variable with the same name will remain as it was, global and with the original value.
# x = "awesome"

# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)

# myfunc()

# print("Python is " + x)

#Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword.
# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x)

# Also, use the global keyword if you want to change a global variable inside a function.
# x = "awesome"

# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x)


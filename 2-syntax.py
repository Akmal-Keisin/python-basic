# Python Indentation
# Indentation refers to the spaces at the beginning of a code line.
# Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.
# Python uses indentation to indicate a block of code.

if 5 > 2:
  print("Five is greater than two!")

# if 5 > 2:
# print("Five is greater than two!")
# Error

# This one fine
if 5 > 2:
    print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 

# if 5 > 2:
# print("Five is greater than two!")
# this one error
#         print("Five is greater than two!")
# There may be times when you want to specify a type on to a variable. 
# This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.
# Casting in python is therefore done using constructor functions:

# int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
# float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
# str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

# Integers
intNum1 = int(12)
intNum2 = int(12.2)
intNum3 = int("12")

print(intNum1)
print(intNum2)
print(intNum3)

# Floats
floatNum1 = float(8)
floatNum2 = float(92.2)
floatNum3 = float("23.2")
floatNum4 = float("3")

print(floatNum1)
print(floatNum2)
print(floatNum3)
print(floatNum4)

# Strings
stringWord1 = str("s1")
stringWord2 = str(2)  
stringWord3 = str(3.0)

print(stringWord1)
print(stringWord2)
print(stringWord3)
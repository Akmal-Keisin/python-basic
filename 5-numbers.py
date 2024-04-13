# There are three numeric types in Python:

# int
# float
# complex

x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))

# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

int1 = 1
int2 = 35656222554887711
int3 = -3255522

print(int1)
print(int2)
print(int3)

# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

float1 = 1.10
float2 = 1.0
float3 = -35.59

print(type(float1))
print(type(float2))
print(type(float3))

# Float can also be scientific numbers with an "e" to indicate the power of 10.

float11 = 35e3
float12 = 12E4
float13 = -87.7e100

print(type(float11))
print(type(float12))
print(type(float13))

# Complex numbers are written with a "j" as the imaginary part:

complex1 = 3+5j
complex2 = 5j
complex3 = -5j

print(type(complex1))
print(type(complex2))
print(type(complex3))

# You can convert from one type to another with the int(), float(), and complex() methods:

intNUm = 1    # int
floatNum = 2.8  # float
complexNum = 1j   # complex

#convert from int to float:
a = float(intNUm)

#convert from float to int:
b = int(floatNum)

#convert from int to complex:
c = complex(intNUm)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Note: You cannot convert complex numbers into another number type.

# Python does not have a random() function to make a random number, 
# but Python has a built-in module called random that can be used to make random numbers:

import random

print(random.randrange(1, 10))
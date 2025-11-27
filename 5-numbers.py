# Practice: Numbers

# Three numeric types
x = 1      # int
y = 2.8    # float
z = 1j     # complex

print(type(x))
print(type(y))
print(type(z))

# Integer examples
int1 = 1
int2 = 35656222554887711
int3 = -3255522

print(int1)
print(int2)
print(int3)

# Float examples
float1 = 1.10
float2 = 1.0
float3 = -35.59

print(type(float1))
print(type(float2))
print(type(float3))

# Scientific notation
float11 = 35e3
float12 = 12E4
float13 = -87.7e100

print(type(float11))
print(type(float12))
print(type(float13))

# Complex numbers
complex1 = 3+5j
complex2 = 5j
complex3 = -5j

print(type(complex1))
print(type(complex2))
print(type(complex3))

# Type conversion
intNum = 1
floatNum = 2.8
complexNum = 1j

# Convert int to float
a = float(intNum)

# Convert float to int
b = int(floatNum)

# Convert int to complex
c = complex(intNum)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Random numbers
import random

print(random.randrange(1, 10))
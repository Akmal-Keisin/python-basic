print(2 + 2)
print(10 - 2 * 12)
print(8 / 4) # division always returns a floating point number

# The integer numbers (e.g. 2, 4, 20) have type int
# The ones with a fractional part (e.g. 5.0, 1.6) have type float

print(4.0 + 2.0) # Float
print(4 + 2) # Int

# Division (/) always returns a float.
# To do floor division and get an integer result you can use the // operator 
# To calculate the remainder you can use %:

print(20 / 2) # Float
print(20 // 2) # Int
print(20 % 3) # Int

# To calculate powers use the ** operator

print(5 ** 2)
print(2 ** 7)

# There is full support for floating point; operators with mixed type operands convert the integer operand to floating point:
print(4 * 3.75 - 1)
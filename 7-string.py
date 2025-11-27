# Practice: Strings

# Creating strings with quotes
print("Hello World")
print('Hello World')

# String variables
stringWord1 = "Hello World"
print(stringWord1)

# Multiline strings
stringParagraph1 = """
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
"""
print(stringParagraph1)

stringParagraph2 = '''
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
'''
print(stringParagraph2)

# Strings as arrays - accessing characters
print(stringWord1[2])

# Looping through strings
for letter in "Hello World":
    print(letter)

# String length
print(len("Hello World"))

# Check if present
print("Hello" in stringWord1)

if "Hello" in stringWord1:
    print("Hello")

# Check if not present
print("Hello" not in stringWord1)

if "Hello" not in stringWord1:
    print("Not Hello")
else:
    print("Hello")

# Slicing
print(stringWord1[2:8])
print(stringWord1[:5])
print(stringWord1[5:])
print(stringWord1[-5:-2])

# String methods
print(stringWord1.upper())
print(stringWord1.lower())
print(stringWord1.strip())
print(stringWord1.replace('World', 'Python!'))
print(stringWord1.split(' '))

# Concatenation
print('Hello' + ' ' + 'World')

# F-strings - combining strings and numbers
age = 20
txt = f"My name is Keisin, I am {age}"
print(txt)

# Escape characters
print("\"That was amazing.\" Larry told me")
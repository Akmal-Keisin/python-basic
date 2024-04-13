# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".
# You can display a string literal with the print() function:

print("Hello World")
print('Hello World')

# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
stringWord1 = "Hello World"
print(stringWord1)

# You can assign a multiline string to a variable by using three quotes:
stringParagraph1 = """
    Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
"""
print(stringParagraph1)

# Or three single quotes:
stringParagraph2 = '''
    Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
'''
print(stringParagraph2)

# Strings are Arrays
# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.

# Get the character at position 1 (remember that the first character has the position 0):
print(stringWord1[2])

# Since strings are arrays, we can loop through the characters in a string, with a for loop.
for letter in "Hello World":
    print(letter)

# To get the length of a string, use the len() function.
print(len("Hello World"))

# To check if a certain phrase or character is present in a string, we can use the keyword in.
print("Hello" in stringWord1)

if "Hello" in stringWord1:
    print("Hello")

# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
print ("Hello" not in stringWord1)
if ("Hello" not in stringWord1):
    print("Not Hello")
else:
    print("Hello")

# Slicing
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.

# Get the characters from position 2 to position 5 (not included):
print(stringWord1[2:8])

# Note: The first character has index 0.

# Slice From the Start
# By leaving out the start index, the range will start at the first character:
print(stringWord1[:5])

# Slice To the End
# By leaving out the end index, the range will go to the end:
print(stringWord1[5:])

# Negative Indexing
# Use negative indexes to start the slice from the end of the string:
print(stringWord1[-5:-2])

# Python has a set of built-in methods that you can use on strings.
# The upper() method returns the string in upper case:
print(stringWord1.upper())

# The lower() method returns the string in lower case:
print(stringWord1.lower())

# The strip() method removes any whitespace from the beginning or the end:
print(stringWord1.strip())

# The replace() method replaces a string with another string:
print(stringWord1.replace('World', 'Python!'))

# The split() method returns a list where the text between the specified separator becomes the list items.
print(stringWord1.split(' '))

# To concatenate, or combine, two strings you can use the + operator.
print('Hello' + ' World')

# we cannot combine strings and numbers like this:
# age = 20
# txt = "My name is Keisin, I am " + age
# print(txt)
# But we can combine strings and numbers by using f-strings or the format() method!

# To specify a string as an f-string, 
# simply put an f in front of the string literal, 
# and add curly brackets {} as placeholders for variables and other operations.

age = 20
txt = f"My name is Keisin, I am {age}"
print(txt)

# A placeholder can contain variables, operations, functions, and modifiers to format the value.

# Escape Character
# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.
# An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

print("\"That was amaizing.\" Larry told me")

# Other escape characters used in Python:
# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value
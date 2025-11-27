# convert age to string and conacatenate with username
username = input("Enter your name: ")
age = 21

greetings = "Hello, " + username + "! You are " + str(age) + " years old."
print(greetings)

# string length
nameLength = len(username)
print("The length of your name is: " + str(nameLength) + " characters.")

# Slicing strings
firstThreeChars = username[:3]
print("The first three characters of your name are: " + firstThreeChars)

# String methods
upperCaseName = username.upper()
print("Your name in uppercase is: " + upperCaseName)

lowerCaseName = username.lower()
print("Your name in lowercase is: " + lowerCaseName)

# Replace part of the string
sentences = "Hello, NAME! Welcome to Java programming."
sentences = sentences.replace("NAME", username)
sentences = sentences.replace("Java", "Python")
print(sentences)

# Count occurrences of a substring
countA = username.count("a")
print("The letter 'a' appears " + str(countA) + " times in your name.")

# Find position of a substring
positionOfE = sentences.find("Python")
print("The position of the word 'Python' in your name is: " + str(positionOfE))

# Escape characters
quote = "He said, \"Python is awesome!\""
print(quote)

multilineString = "This is line one.\nThis is line two.\nThis is line three."
print(multilineString)

tabString = "Column1\tColumn2\tColumn3"
print(tabString)

# Formating string using f-strings
formattedString = f"Hello, {username}! Next year, you will be {age + 1} years old."
print(formattedString)
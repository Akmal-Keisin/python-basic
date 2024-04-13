# Booleans represent one of two values: True or False.
# When you compare two values, the expression is evaluated and Python returns the Boolean answer:
print(19 > 11)
print(12 == 3)
print(412 < 239)

# When you run a condition in an if statement, Python returns True or False:
x = 231
y = 112

if x > y:
    print(f"{x} is greater than {y}")
else:
    print(f"{y} is greater than {x}")

# The bool() function allows you to evaluate any value, and give you True or False in return,
print(bool(12))
print(bool("Hello World"))

# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.

# True
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

# False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

# Functions can Return a Boolean
def boolFunction():
   return True

if boolFunction():
   print("The function is True")
else:
   print("The function is False")
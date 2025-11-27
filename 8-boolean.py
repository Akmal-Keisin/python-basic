# Practice: Boolean

# Boolean values from comparisons
print(19 > 11)
print(12 == 3)
print(412 < 239)

# Booleans in conditionals
x = 231
y = 112

if x > y:
    print(f"{x} is greater than {y}")
else:
    print(f"{y} is greater than {x}")

# The bool() function
print(bool(12))
print(bool("Hello World"))

# Values that evaluate to True
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

# Values that evaluate to False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# Objects with __len__ method
class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))

# Functions returning Boolean
def boolFunction():
    return True

if boolFunction():
    print("The function is True")
else:
    print("The function is False")
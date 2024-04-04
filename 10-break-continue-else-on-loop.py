# The break statement breaks out of the innermost enclosing for or while loop.
# A for or while loop can include an else clause.
# In a for loop, the else clause is executed after the loop reaches its final iteration.
# In a while loop, it’s executed after the loop’s condition becomes false.
# In either kind of loop, the else clause is not executed if the loop was terminated by a break.
# This is exemplified in the following for loop, which searches for prime numbers:

for number in range(2, 5):
    for target in range(2, number):
        if (number % target == 0):
            print(number, 'equals', target, '*', number//target)
            break
    else:
        # Loop feel through without finding a factor
        print(number, 'is a prime number')

# The continue statement, also borrowed from C, continues with the next iteration of the loop:

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)
'''
You will be provided with a random number in a variable called num.

Use a conditional statement to check if the number is odd. if num is odd, 
print "odd". Otherwise print "even".

Hint: use modulus % to figure out if the number id odd!
'''

# NO TOUCHING ======================================
from random import randint
num = randint(1, 1000) #picks random number from 1-1000
# NO TOUCHING ======================================

# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
if num % 2 != 0:
    print("odd")
else:
    print("even")

# YOUR CODE GOES HERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
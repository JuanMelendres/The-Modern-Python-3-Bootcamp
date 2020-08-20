'''
At the top of the file some starter code that randomly picks a number between 1 and 10, 
and save it to a variable called choice. Don´t touch those lines! (please)

Your job is to wirte a simple conditional to check if choice is 7. if choice is 7,
print out "lucky". Otherwise, print out "unlucky"
'''

# NO TOUCHING PLEASE---------------
from random import randint
choice = randint(1,10)
# NO TOUCHING PLEASE---------------

# YOUR CODE GOES HERE:
if choice != 7:
    print("unlucky")
else:
    print("lucky")

# Basic solution
'''
if choice == 7:
    print("lucky")
else:
    print("unlucky")
'''
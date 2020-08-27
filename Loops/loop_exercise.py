'''
For Loop and Range Exercise
Use a for loop to add up every odd number from 10 to 20 (inclusive) and store the result in the variable x.
You could cheat and just figure this using a calculator, but...that would defeat the whole point of this course. 
'''
# Add up all odd numbers between 10 and 20
# Store the result in x:
x = 0

# YOUR CODE GOES HERE:

# Solution Using a Conditional
for num in range(10, 21):
    if num % 2 != 0:
        x += num

# Solution using range step
for i in range(11,21,2):
        x += i
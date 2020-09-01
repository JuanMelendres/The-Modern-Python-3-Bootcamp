import random

rando_number = random.randint(1, 10) # Random number between 1 - 10

'''
handle user guesses
* If the user guess correct, tell them they won
* Otherwise tell them if they are too high or too low
Bonus - let the player play agin if they want!
'''
guess = None

while guess != rando_number:
    guess = input("Pick a number from 1 to 10: ")
    guess = int(guess)
    if guess == rando_number:
        print("YOU GOT IT!")
    elif guess < rando_number:
        print("TOO LOW!")
    else:
        print("TOO HIGH!")
print(rando_number)
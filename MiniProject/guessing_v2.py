import random

rando_number = random.randint(1, 10) # Random number between 1 - 10

'''
handle user guesses
* If the user guess correct, tell them they won
* Otherwise tell them if they are too high or too low
Bonus - let the player play agin if they want!
'''
guess = None

while True:
    guess = input("Pick a number from 1 to 10: ")
    guess = int(guess)
    if guess < rando_number:
        print("TOO LOW!")
    elif guess > rando_number:
        print("TOO HIGH!")
    else:
        print("YOU GOT IT!")
        print(rando_number)
        play_again = input("Do you want to play again? (y/n) ")
        if play_again == "y":
            rando_number = random.randint(1, 10)
            guess = None
        else:
            print("Thank you for playing!")
            break

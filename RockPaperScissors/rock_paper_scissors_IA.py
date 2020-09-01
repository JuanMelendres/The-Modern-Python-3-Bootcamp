from random import randint

print("Rock...")
print("Paper...")
print("Scissors...")

player = input("Player 1, make your move: ").lower()

rand_num = randint(0,2)

if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"

print(f"IA plays {computer}")

if player:
    if player == computer:
        print("It`s a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("Player1 wins!")
        else:
            print("IA wins!")
    elif player == "paper":
        if computer == "rock":
            print("Player1 wins!")
        else:
            print("IA wins!")
    elif player == "scissors":
        if computer == "paper":
            print("Player1 wins!")
        else:
            print("IA wins!")
    else:
        print("something went wrong")
else:
    print("something went wrong")
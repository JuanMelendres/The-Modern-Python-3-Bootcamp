from random import randint

player_wins = 0
computer_wins = 0
winning_score = 3

while player_wins < winning_score and computer_wins < winning_score:
    print(f"Player Score: {player_wins} Computer Score: {computer_wins}")
    print("...Rock...")
    print("...Paper...")
    print("...Scissors...")

    player = input("Player 1, make your move: ").lower()

    if player == "quit" or player == "q":
        break

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
                print("Player wins!")
                player_wins += 1
            else:
                print("IA wins!")
                computer_wins += 1
        elif player == "paper":
            if computer == "rock":
                print("Player wins!")
                player_wins += 1
            else:
                print("IA wins!")
                computer_wins += 1
        elif player == "scissors":
            if computer == "paper":
                print("Player wins!")
                player_wins += 1
            else:
                print("IA wins!")
                computer_wins += 1
        else:
            print("something went wrong")
    else:
        print("something went wrong")

if player_wins > computer_wins:
    print("CONGRATS, YOU WON!")
elif player_wins == computer_wins:
    print("OH IT'S A TIE!")
else:
    print("OH NO :( THE COMPUTER WON!")

print(f"Final Scores... Player Score: {player_wins} Computer Score: {computer_wins}")
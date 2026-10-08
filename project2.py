import random

# initializing
game = ['rock', 'paper', 'scissors']

while True:

    pscore = 0
    cscore = 0

    print("\n===== ROCK PAPER SCISSORS =====")
    print("Best of 3")

    while pscore < 2 and cscore < 2:

        # taking input from user
        player = input(
            "\nEnter your choice (rock, paper, scissors, random): "
        ).lower()

        if player == 'random':
            player = random.choice(game)
            print(f"You randomly chose: {player}")

        # checking invalid input
        if player not in game:
            print("Invalid input! Please enter rock, paper, scissors or random.")
            continue

        computer = random.choice(game)
        print(f"Computer chose: {computer}")

        # checking winner
        if player == computer:
            print("It's a tie!")

        elif player == 'rock' and computer == 'scissors':
            print("You win!")
            pscore += 1

        elif player == 'paper' and computer == 'rock':
            print("You win!")
            pscore += 1

        elif player == 'scissors' and computer == 'paper':
            print("You win!")
            pscore += 1

        else:
            print("Computer wins!")
            cscore += 1

        # showing score after every round
        print("----------------")
        print("Your score:", pscore)
        print("Computer score:", cscore)
        print("----------------")

    # final winner
    if pscore == 2:
        print("\n🎉 YOU WON THE MATCH!")
    else:
        print("\n💻 COMPUTER WON THE MATCH!")

    # final score
    print("Final Score:")
    print("You:", pscore)
    print("Computer:", cscore)

    # replay
    replay = input("\nDo you want to play again? (yes/no): ").lower()

    if replay != 'yes':
        print("Thanks for playing!")
        break
import random


def getchoices():
    player_choice = input("Enter a choice (rock, paper, scissors:)")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def check_win(player, computer):
    print(f"you chose {player} computer chose {computer}")
    if player == computer:
        return "its a tie"

    elif player == "rock":
        if computer == "scissors":
            return "rock smashes scissors! you Win"
        else:
            return "paper covers rock! You lose."

    elif player == "paper":
        if computer == "rock":
            return "paper covers rock! you Win"
        else:
            return "scissors cuts paper! You lose."

    elif player == "scissors":
        if computer == "paper":
            return "scissors cuts paper! you Win"
        else:
            return "rock smashes scissors! You lose."


choices = getchoices()

result = check_win(choices["player"], choices["computer"])
print(result)

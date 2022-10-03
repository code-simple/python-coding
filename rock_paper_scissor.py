import random

user_wins = 0
computer_wins = 0
option = ["rock", "paper", "scissor"]

while True:
    user_input = input("Type Rock / Paper / Scissor or Q to Quite: ").lower()

    if user_input == "q":
        break

    if user_input not in option:
        print("Wrong Input")
        continue

    random_number = random.randint(0, 2)
    computer_pick = option[random_number]
    print("Computer pick ", computer_pick)

    if user_input == "rock" and computer_pick == "scissor":
        print("You Won")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You Won")
        user_wins += 1
    elif user_input == "scissor" and computer_pick == "paper":
        print("You Won")
        user_wins += 1
    else:
        print("You Lost")
        computer_wins += 1

print("You Wins : ", user_wins, " Computer Wins : ", computer_wins)
print("GoodBye !")

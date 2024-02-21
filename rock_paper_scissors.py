import random

user_wins = 0
computer_wins = 0

options  = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/scissors or Q to Quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue
    
    random_number = random.randint(0, 2)

    computer_pick = options[random_number]
    print("Computer picked", computer_pick)

    if user_input == "rock" and computer_pick == "scissors":
        print("you won")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("you won")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("you won")
        user_wins += 1

    elif user_input == "rock" and computer_pick == "rock":
        print("It´s a tie")

    elif user_input == "paper" and computer_pick == "paper":
        print("It´s a tie")

    elif user_input == "scissors" and computer_pick == "scissors":
        print("It´s a tie")

    else:
        print("you lost!")
        computer_wins += 1
        continue

    if computer_wins or user_wins == 3:
        break


print("you won", user_wins, "times")
print("The computer won", computer_wins, "times")
print("GoodBye")

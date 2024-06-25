# Created by Arav Neroth on 06/24/2024

import random

while True:
    options = ["rock", "paper", "scissors"]

    computer = random.choice(options)
    player = None

    while player not in options:
        player = input("Choose one of the following: rock | paper | scissors : ").lower()

    # Tie Scenario 
    if player == computer:
        print("Your Choice: " , player)
        print("Computer's Choice: " , computer)
        print("It's a Tie!")
    
    # Player Wins   
    elif player == options[0] and computer == options[2]:
        print("Your Choice: " , player)
        print("Computer's Choice: " , computer)
        print("You Win!")

    elif player == options[1] and computer == options[0]:
        print("Your Choice: " , player)
        print("Computer's Choice: " , computer)
        print("You Win!")

    elif player == options[2] and computer == options[1]:
        print("Your Choice: " , player)
        print("Computer's Choice: " , computer)
        print("You Win!")

    # Player Looses   
    elif player == options[0] and computer == options[1]:
        print("Your Choice: " , player)
        print("Computer's Choice: " , computer)
        print("You Loose")

    elif player == options[1] and computer == options[2]:
        print("Your Choice: " , player)
        print("Computer's Choice: " , computer)
        print("You Loose")

    elif player == options[2] and computer == options[0]:
        print("Your Choice: " , player)
        print("Computer's Choice: " , computer)
        print("You Loose")
    
    # looping 
    another_round = input("Would you like to play again: yes | no : ").lower()
    print("--------------------------------------------------------")

    if another_round != "yes":
        break

print("Thanks for playing!")
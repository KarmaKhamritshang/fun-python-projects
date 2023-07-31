#!/usr/bin/python3

# ------------------------------------------------------------------------
# Name  : rps.py
# Source: C:\Users\karma\Projects\000_Python\Projects\rps.py
# Description: Simple Rock Paper Scissors game in Python
# Author: Karma Khamritshang
# ------------------------------------------------------------------------

import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper OR scissors?: ").lower()

    if player == computer:
        print("Computer: ",computer)
        print("Player: ", player)
        print("Tie!")

    elif player == "rock":
        if computer == "paper":
            print("Computer: ",computer)
            print("Player: ", player)
            print("You lost!")
        if computer == "scissors":
            print("Computer: ",computer)
            print("Player: ", player)
            print("You won!")

    elif player == "scissors":
        if computer == "rock":
            print("Computer: ",computer)
            print("Player: ", player)
            print("You lost!")
        if computer == "paper":
            print("Computer: ",computer)
            print("Player: ", player)
            print("You won!")

    elif player == "paper":
        if computer == "scissors":
            print("Computer: ",computer)
            print("Player: ", player)
            print("You lost!")
        if computer == "rock":
            print("Computer: ",computer)
            print("Player: ", player)
            print("You won!")
            
    play_again = input("Wanna play again? (yes/no): ").lower()
    
    if play_again != "yes":
        break
print("Bye!")
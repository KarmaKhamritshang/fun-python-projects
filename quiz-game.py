#!/usr/bin/python3

# ------------------------------------------------------------------------
# Name  : quiz-game.py
# Source: C:\Users\karma\Projects\000_Python\Projects\quiz-game.py
# Description: Simple Quiz game in Python
# Author: Karma Khamritshang
# ------------------------------------------------------------------------

import os

# ------------------------------------------------------------------------

questions = { #dictionary
    " Who created Python?: ": "A",
    " What year was Python created?: ": "B",
    " Python is tributed to which comedy group?: ": "C",
    " Is the Earth round?: ": "A"
}

options = [[" A. Guido van Rossum", " B. Elon Musk", " C. Bill Gates", " D. Mark Zuckerberg"], #2d list - tuples
          [" A. 1989", " B. 1991", " C. 2000", " D. 2016"],
          [" A. Lonely Island", " B. Smosh", " C. Monty Python", " D. SNL"],
          [" A. True", " B. False", " C. sometimes", " D. What's Earth?"]]

# ------------------------------------------------------------------------

def new_game():
    
    guesses = []
    correct_guesses = 0
    question_num = 1
    
    for key in questions:
        print("")
        print(key)
        print("------------------------------------------")
        for i in options[question_num-1]:
            print(i)
        
        print("------------------------------------------")
        guess = input("Enter (A, B, C or D): ").upper()
        
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1
        clear_screen()
        
    display_score(correct_guesses, guesses)
    

# ------------------------------------------------------------------------   
    
def clear_screen():
    # Check if the OS is Windows
    if os.name == 'nt':
        os.system('cls')
    else:  # Assume Unix-based system
        os.system('clear')
# ------------------------------------------------------------------------

def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0
    
# ------------------------------------------------------------------------

def display_score(correct_guesses, guesses):
    print("")
    print(" RESULTS")
    print("------------------------------------------")
    print(" Solution: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print(" My Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print("")
    print("------------------------------------------")
    score = int((correct_guesses/len(questions)*100))
    print("Your score is: "+str(score)+"%")
    print("------------------------------------------")
    
# ------------------------------------------------------------------------

def play_again():
    response = input("Do you want to play again? (yes or no): ").upper()
    if response == "YES":
        return True
    else:
        return False
    
# ------------------------------------------------------------------------

clear_screen()
new_game()

while play_again():
    new_game()

print("Byeee!")

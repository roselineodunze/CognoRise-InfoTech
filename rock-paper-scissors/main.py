from random import *

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

is_user_winner = None
is_game_on = True
game_art = [rock, paper, scissors]
computer_score = 0
user_score = 0

def play_again():
    play = input("Do you want to play again, y or n: ").lower()
    if play == "y":
        return True
    elif play == "n":
        return False
    else:
        print("Invalid response")
        play_again()

while is_game_on:
    user_input = int(input("Pick rock, paper or scissors. Type 0, 1 or 2 respectively: "))
    print(f"User picked:\n {game_art[user_input]}")

    computer_input = randint(0, 2)
    print(f"Computer picked:\n {game_art[computer_input]}")

    if user_input > computer_input:
        if user_input == 2 and computer_input == 0:
            is_user_winner = False
        else:
            is_user_winner = True
    elif user_input == computer_input:
        print("It is a draw")
    else:
        if user_input == 0 and computer_input == 2:
            is_user_winner = True
        else:
            is_user_winner = False

    if is_user_winner:
        user_score += 1
        print("💪 User wins this round")
    else:
        print("🦾 Computer wins this round")
        computer_score += 1
    print(f"User: {user_score}\nComputer: {computer_score}")

    if play_again():
        is_game_on = True
    else:
        is_game_on = False


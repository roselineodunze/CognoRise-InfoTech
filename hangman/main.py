import random
from art import stages, logo
from words import word_list

print(logo)

lives = 6
game_over = False

rand_word = random.choice(word_list)
display = []
for x in range(len(rand_word)):
    display.append("_")

def game_over():
    if lives >= 1:
        if "_" not in display:
            print(f"You guessed the word {display} correctly 🥳 ")
            return True
        else:
            return False
    else:
        print("Game over. The man was hanged. 😢")
        print(f"The word is {rand_word}")
        return True

while not game_over():
    print(f"Word o guess is: {display}")
    user_guess = input("guess a letter: ").lower()
    if user_guess in display:
        print(f"You have already guessed {user_guess}")

    for x in range(len(rand_word)):
        if rand_word[x] == user_guess:
            display[x] = user_guess
            print("You guessed another letter ✅")

    if user_guess not in rand_word:
        lives -= 1
        print(stages[lives])
        print(f"Your guess is wrong ❌, remaining life is {lives}")

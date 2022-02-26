# Guess the number game

import random
randNumber = random.randint(1,500)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter your Guess: "))
    guesses += 1
    if(userGuess==randNumber):
        print("You guessed the number right!")
    else:
        if(userGuess>randNumber):
            print("You guessed the number wrong. Please enter a small number")
        else:
            print("you guessed the number wrong. Please enter a large number.")

print(f"You have guessed the number in {guesses} guesses")
with open("highscore.txt", "r") as f:
    highscore = int(f.read())

if(guesses<highscore):
    print("Hurray! You have broken the high score!")
    with open("highscore.txt", "w") as f:
        f.write(str(guesses))
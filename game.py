import random


def ask_level():
    while True:
        level = input("Please type easy, medium or hard: ")
        if level == "easy":
            return 10
        elif level == "medium":
            return 100
        elif level == "hard":
            return 1000
        else:
            print("easy or medium or hard!! All lowercase please ")


def ask_guess(top):
    while True:
        try:
            guess = int(input(f"Guess a number from 1 to {top}: "))
            return guess
        except ValueError:
            print("Type a number")


def play_game(top):
    secret = random.randint(1, top)
    attempts = 1
    guess = ask_guess(top)
    while secret != guess:
        if secret < guess:
            print("Too High")
        else:
            print("Too Low")
        attempts += 1
        guess = ask_guess(top)
    print("Matched!!!")
    return attempts


answer = "y"
best = 5000
while answer == "y":
    top = ask_level()
    score = play_game(top)
    print(f"The attempts were {score}")
    if score < best:
        best = score
    print(f"Best so far: {best} attempts")
    answer = input("Want to play again? y/n ")
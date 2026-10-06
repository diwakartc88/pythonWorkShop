import random

def ask_guess():
    while True:
        try: 
            guess = int(input("Guess a number from 1 to 100: "))
            return guess
        except ValueError:
            print("Type a number")


def play_game():
    secret = random.randint(1, 100)
    attempts = 1
    guess = ask_guess()
    while secret != guess:
        if secret < guess:
            print("Too High")
        else:
            print("Too Low")
        attempts += 1
        guess = ask_guess()
    print("Matched!!!")
    return attempts

answer = "y"
best = 5000
while answer == "y":
    score = play_game()
    print(f"The attempts were {score}")
    if score < best:
        best = score
    print(f"Best so far: {best} attempts") 
    answer = input("Want to play again? y/n ")
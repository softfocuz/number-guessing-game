import random

TARGET_SCORE = 5

name = input("Enter Your Name: ")
number = random.randint(1,100)
score = 0

while score < TARGET_SCORE:
    user_guess = int(input("Enter Your Guess: "))
    if user_guess == number:
        score += 1
        print(f"Score: {score}/{TARGET_SCORE}")

        if score < TARGET_SCORE:
            number = random.randint(1, 100)

    elif user_guess < number:
        print("Your Guess is Low")
    else:
        print("Your Guess is High")

print(f"Congratulations {name}!\nSCORE: {score}/{TARGET_SCORE}")
